

import scapy.all as scapy

def scan(ip):
    arp_request= scapy.ARP(pdst= ip)
    broadcast= scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast= broadcast/arp_request

    #print(arp_req_broadcast.summary())
        #this line can show u arp message

    #arp_req_broadcast.show()
        #show us more details of the content of packet


scan("192.168.1.1/24")
