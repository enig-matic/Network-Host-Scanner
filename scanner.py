import scanner_port as p
import scanner_host as h
import scanner_banner as b
import pyfiglet

name = "JANGOTRA"
print ("=" * 60)

ban = pyfiglet.figlet_format(
    name,
    font="slant"
)

print("\033[96m" + ban + "\033[0m")
print("=" * 60)
print("       Host Online, Open Port, Banner Grabbing")

print("=" * 60)
print('       Online 1 host-port and that port have banner')
print('       If available, You can check only once in every input')
print("=" * 60)
print("Date : 26/10/2026\n")


if __name__ == "__main__":

    print("\nMake sure you enter right IP Address")

    # Enter the Target IP Address
    ip = input("\nTry to Check whether the Host is Online or Ofline: ")

    if h.scan_host(ip): 
        # Check wherther the host is live or not 
        # if host is ofline then if condition will not execute

        POrt = int(input("\nEnter the Port Number: ")) 
        # take port input as a integer because only scan single port 

        print("Scanning Port...\n")

        open_port = p.scan_port(ip,POrt) 
        # Check whether the port is open or not 

        if open_port :
            # if port is open , then this if Statement is execute otherwiese not
            print(f"Host: {ip} is online\nPort: {POrt} is open")

            Banner = input(f"\nAre you check the banner if Available (y,n):").lower()
            # if you want to check that this port give banner or not 

            if Banner == 'y':
                check_banner = b.scan_banner(ip,POrt) 
                # Check if the banner is available on this particular port 

                if check_banner :
                    #if banner is found then this if statement is execute otherwise not
                    print(f"\nBanner Found!\n\n{check_banner}")
                else :
                    print("Banner Not Found!")

        else :
            # if host is online but not port is open 
            print(f"Host: {ip} is online\nPort: {POrt} is closed")

    else:
        # if host is ofline
        print(f"Host: {ip} is Ofline\nEnter Valid Host.")