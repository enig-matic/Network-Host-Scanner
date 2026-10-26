from scapy.all import TCP,ICMP,IP,sr1

def scan_host(ip):

        
    response = sr1(IP(dst=str(ip))/ICMP(),verbose =0, timeout=1)
        # send the icmp request to check the host is online or ofline
        # if host is ofline, then response have None value 

    if response is not None :
        return True
    
    return False