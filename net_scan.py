 #!/usr/bin/env python

import scapy.all as scapy

def scan(ip): 
    arp_request = scapy.ARP(pdst = ip)
    # arp_request.pdst = ip
    # arp_request.show()  #(show all fields in the ARP )
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff")
    # broadcast.dst = "ff:ff:ff:ff:ff:ff"
    # broadcast.show()
    arp_request_broadcast = broadcast/arp_request
    # arp_request_broadcast.show()
    # print(arp_request_broadcast.summary())
    answered_list = scapy.srp(arp_request_broadcast,timeout=1)[0]
    # answered_list is in form  of a list
    clients_list = []

    print('IP\t\t**\t\tMAC_ADDRESS\n******************************************************************')
    for answer in answered_list:
        client_dict = {"ip":answer[1].psrc,"mac":answer[1].hwsrc}
        clients_list.append(client_dict)
    return clients_list

scan_results=scan("20.20.20.1/24")

def print_result(results_list):
    
    for client in results_list:
        print(client["ip"] + "\t\t\t" + client["mac"] )

print_result(scan_results)

