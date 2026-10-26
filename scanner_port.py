from scapy.all import TCP,ICMP,IP,sr1

def scan_port(ip,port):
    for host in [ip]:


    # To check whether the port is open or not 
    # if port is not open, then it return None value

        response = sr1(
        IP(dst=host)/
        TCP(dport=port, flags='S'),
        verbose=0,
        timeout=1
        )

        # response.haslyer(Tcp) means if the packet contain TCP (segment)
        # if response is not None and packet contain TCP segment then the if statement will execute

        if response and response.haslayer(TCP):

            tcp = response.getlayer(TCP)
            # response.getlayer(TCP) means get the TCP from the packet and store it to the tcp variable

            if tcp.flags & 0x12 == 0x12 :
                #0x12  is to represent hexadecimal which represent to  SYN-ACK  flags during TCP handshake 
                # tcp.flags have 8 bits , & = bitwise operator , it commpare the tcp.flag and 0x12 value which is equal to 0x12 , then this if statement will execute

                return True
            
    return False
