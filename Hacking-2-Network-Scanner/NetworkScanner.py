import scapy.all as scapy
import optparse

# pip/pip3 install scapy then write one bottom 
# python NetworkScanner.py -ip 10.0.2.1/24
# python3 NetworkScanner.py --ip_adress 10.0.2.1/24

#1 - arp request
#2 - broadcast
#3 - response

def get_user_parameters():
    parse_object = optparse.OptionParser()
    parse_object.add_option("-i", "--ip_adress", dest="ip_adress", help="Enter ip adress")
    (user_input, arguments) = parse_object.parse_args()
    if not  user_input.ip_adress :
        print("Enter ip adress")
    return user_input

def scan_my_ip(ip):
    arp_request = scapy.ARP(pdst = ip)
    #scapy.ls(scapy.ARP())       # get info
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    #scapy.ls(scapy.Ether())     # get info

    combined_packet = broadcast/arp_request
    (answered_list, unanswered_list) = scapy.srp(combined_packet,timeout = 1)
    answered_list.summary()
    # print(list(answered_list))
    # print(unanswered_list)

user_ip_adress = get_user_parameters()
print(str(user_ip_adress.ip_adress))
scan_my_ip(user_ip_adress.ip_adress)

