import scapy.all as scapy

def scan(ip):
    arp_request= scapy.ARP(pdst= ip)
    broadcast= scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast= broadcast/arp_request
    answered_list = scapy.srp(arp_req_broadcast,timeout = 1, verbose=False)[0]
    client_list=[]
    for element in answered_list :
        client_dict= {"IP":element[1].psrc,"MAC":element[1].hwdst}
        client_list.append(client_dict)
    print(client_list)

scan("192.168.1.1/24")