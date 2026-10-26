import socket

def scan_banner(ip,port):
    try:

        # Af_NET means we use IPv4 address to make connection 
        #SOCK_STREAM means we send packet in stream with a partcular stream number, this is a TCP concept if you want to learn, then you must try to capture packet in wireshark
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        # this statement means if the response is not come within 3 second ,then stop and break the connection
        sock.settimeout(3)

        # ip = add target ip to establish the connection
        # port = which you want to make connection on particular prot
        sock.connect((ip,port))

        # we generate http request, which server send our banner but sometime it will not happen 
        # b means we send data to server in bytes
        sock.send(b"GET / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")

        # this statement means we receive 1024 byte at a time
        banner = sock.recv(1024)

        # this statement means close the connection 
        sock.close()

         # this statement means decode all the byte and if generate error then ignore it , this error do lose some data  
        return banner.decode('utf-8',errors='ignore')


        # if no response come from the server, then we see Execption then return None 
    except Exception:
        return None

