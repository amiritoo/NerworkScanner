import scapy.all as scapy

def scan(ip):
    arp_request= scapy.ARP(pdst= ip)
    broadcast= scapy.Ether(dst= "ff:ff:ff:ff:ff:ff")
    arp_req_broadcast= broadcast/arp_request
    answered_list = scapy.srp(arp_req_broadcast,timeout = 1, verbose=False)[0]
    client_list=[]

    for element in answered_list :
        client_dict= {"IP":element[1].psrc,"MAC":element[1].hwsrc}
        client_list.append(client_dict)
    return client_list

def print_result(list_of_clients):
    print("IP\t\t\tMAC\n-------------------------------------")
    for client in list_of_clients:
        print(client["IP"] + "\t\t" + client["MAC"])


final_result= scan("192.168.1.1/24")
print_result(final_result)
