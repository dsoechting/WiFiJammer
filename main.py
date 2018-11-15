import pyrcrack
import nmap

ip = '10.202.208.1-30'
ports = '80'
nm = nmap.PortScanner()
nm.scan(ip, ports)
print("scan info")
print(nm.scaninfo())
print("")
print("hosts:")
print(nm.all_hosts())
print("")
print("hostnames:")
print(nm[ip].hostnames())
