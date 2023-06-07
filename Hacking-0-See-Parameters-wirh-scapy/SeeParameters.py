import scapy.all as scapy

scapy.ls(scapy.ARP())

# psrc = your ip
# hwsrc = your mac
# op = 1  for request
# op = 2  for response
# pdst = target ip
# hwdst = target mac
#
