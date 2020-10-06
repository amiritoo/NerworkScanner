
import scapy.all as scapy

def scan(ip):
    arp_request= scapy.ARP(pdst= ip)
    broadcast= scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast= broadcast/arp_request
    answered,unasnwerd = scapy.srp(arp_req_broadcast,timeout = 1)



scan("192.168.1.1/24")
