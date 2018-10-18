import scapy.all as scapy


def scan(ip):
    packet_request = scapy.ARP(pdst=ip)
    broadcast_dest = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
    full_bar = broadcast_dest/packet_request

    answers = scapy.srp(full_bar,timeout=1,verbose=False)[0]
    for answer in answers:
        print ({'ip':answer[1].psrc,'mac':answer[1].hwsrc})


scan('20.20.21.1/24')