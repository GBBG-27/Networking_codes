#!/bin/python3
import socket


try:
     name_index = socket.if_nameindex()

     for inter_info in name_index:
       
           index = inter_info[0]
           name = inter_info[1]
            
           if name == 'eth0':
      
                INTERFACE = name 
                ETHERTYPE = socket.ETHERTYPE_ARP
except KeyboardInterrupt:
       print('\n')
except Exception as exc:
       print(exc)


try:

    with socket.socket(socket.AF_PACKET , socket.SOCK_RAW) as sock:
            if INTERFACE is not None:
            
                sock.bind((INTERFACE , ETHERTYPE)) 
            
                with open("RECEIVING_ARP_PACKETS.txt"  , 'w' )  as packet_file:
                     
                        packet_file.write('ARP_PACKETS\n')
                        packet_file.write(f'{"*" * 13}\n')
                      
                        while True:
                          
                              recv_packet = sock.recv(100024)
                              decode_packets = recv_packet.decode(errors='ignore')
                              n_bytes = packet_file.write(decode_packets)
                              print(f'Sent [{n_bytes}] to file')

except KeyboardInterrupt:
      print('\n')
except Exception as exc:
      print(exc)
 
                                                   
         
         
          
