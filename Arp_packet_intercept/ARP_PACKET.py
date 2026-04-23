#!/bin/python3
import socket
# This is a simple script that is that itercept only ARP(Address Resolution Protocol)
# packets on a network  interface,it
# tries to decode it with utf-8 and ignores the bytes that can not 
# be decoded


try: # This is for catching errors and exceptions 

     # this returns a tuple of the network inteface and is's index on the machine
     name_index = socket.if_nameindex()

     # this will loop through the name and interface returned from name_index
     for inter_info in name_index:

           index = inter_info[0] # the interface index retrieved
           name = inter_info[1] # the interface name retrieved
           
           # cross-check if the name is "eth0"
           # you can change this to your prefered interface 
           if name == 'eth0':
      
                INTERFACE = name # assign a variable to the interface name
                ETHERTYPE = socket.ETHERTYPE_ARP # assign a variable to the ETHERTYPE to use
                
except KeyboardInterrupt: # catching keyboard Interruption
       print('\n')
except Exception as exc: # catching any other exception
       print(exc)


# this will catch exceptions and errors
try:
    # a context manager that create a socket object and assign a name to it   
    with socket.socket(socket.AF_PACKET , socket.SOCK_RAW) as sock:

            # cross-check if there is a value in interface 
            if INTERFACE is not None:

                # bind the socket object with the interface name and ethertype  
                sock.bind((INTERFACE , ETHERTYPE)) 

                # open a file and write the decoded data to it
                # Note: the file must be in the current directory or location where the script is 
                with open("RECEIVING_ARP_PACKETS.txt"  , 'w' )  as packet_file:

                        # some extra data written to the file
                        packet_file.write('ARP_PACKETS\n')
                        packet_file.write(f'{"*" * 13}\n')

                        # a loop to receive the packet,decode it and send it to the file 
                        while True:

                              recv_packet = sock.recv(100024) # receive the packet
                              decode_packets = recv_packet.decode(errors='ignore') # decode the packet 
                              n_bytes = packet_file.write(decode_packets) # write it to the file
                              print(f'Sent [{n_bytes}] to file') # this executes every time data is written to the file

except KeyboardInterrupt: # catching keyboard interruption
      print('\n')
except Exception as exc: # catching any other error
      print(exc)


