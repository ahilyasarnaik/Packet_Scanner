import pyfiglet
import socket
from datetime import datetime

ascii_banner = pyfiglet.figlet_format("PORT SCANNER")
print(ascii_banner)

def port_scanner(target, start_port, end_port):
    # Display a banner with information about the scan
    print("-" * 50)
    print(f"Scanning Target: {target}")
    print(f"Scanning started at: {datetime.now()}")
    print("-" * 50)

    try:
        # Iterate through the specified range of ports
        for port in range(start_port, end_port + 1):
            # Create a socket object
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)

            # Attempt to connect to the target and port
            result = s.connect_ex((target, port))

            # Check if the connection was successful (port is open)
            if result == 0:
                print(f"Port {port} is open")

            # Close the socket
            s.close()

    except KeyboardInterrupt:
        print("\nExiting Program!")
        exit()
    except socket.gaierror:
        print("\nHostname Could Not Be Resolved!")
        exit()
    except socket.error:
        print("\nServer not responding!")
        exit()

    # Display scan completion time
    print("-" * 50)
    print(f"Scanning finished at: {datetime.now()}")
    print("-" * 50)

if __name__ == "__main__":
    # Specify the target, start port, and end port for the scan
    target_ip = input("Enter the target IP address: ")
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Perform the port scan
    port_scanner(target_ip, start_port, end_port)
