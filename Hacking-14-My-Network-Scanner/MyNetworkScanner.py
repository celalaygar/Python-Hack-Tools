from scapy.all import ARP, Ether, srp

def arp_scan(ip):
    arp_request = ARP(pdst=ip)
    broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

def print_result(result_list):
    print("IP Address\t\tMAC Address")
    print("----------------------------------------------------")
    for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])

ip_range = "192.168.1.1/24"  # İp aralığınızı buraya girin (örneğin, 192.168.1.1/24)

scan_result = arp_scan(ip_range)
print_result(scan_result)
