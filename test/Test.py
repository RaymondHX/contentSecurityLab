import pcap
# list all of the Internet devices
devs = pcap.findalldevs()
print(*devs, sep='\n')
pc = pcap.pcap(devs[3], promisc=True, immediate=True, timeout_ms=50)
# fiter http pcakets
pc.setfilter('tcp port 80')
for ptime, pdata in pc:
    print(ptime, pdata)