
import scapy.all as scapy

def scan(ip):
    arp_request= scapy.ARP(pdst= ip)
    broadcast= scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast= broadcast/arp_request
    answered_list = scapy.srp(arp_req_broadcast,timeout = 1, verbose=False)[0]
    print("IP\t\t\tMAC\n-------------------------------------")
    for element in answered_list :
        print(element[1].psrc + "\t\t\t" + element[1].hwdst)

scan("192.168.1.1/24")
