# Packet_Scanner
Imports:

socket: The Python socket library is used to create network sockets and perform network-related operations.
datetime: This module provides functions to work with dates and times.
port_scanner Function:

This function takes three parameters: target (the target IP address), start_port, and end_port (the range of ports to scan).
It creates a socket and attempts to connect to each port in the specified range on the target.
If the connection is successful (result == 0), it prints that the port is open.
The function catches keyboard interrupt, socket errors, and hostname resolution errors and exits gracefully.
It also prints a banner displaying information about the scan start and finish.
if __name__ == "__main__": Block:

This block executes when the script is run directly (not imported as a module).
It prompts the user to input the target IP address, start port, and end port.
It then calls the port_scanner function with the provided inputs to perform the port scan.
Usage:

Run the script (python port_scanner.py).
Enter the target IP address and the range of ports you want to scan when prompted.
The script will display information about the scan and report open ports.
