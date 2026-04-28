#!/bin/python3

import socket


def packet_socket(Interface , ether_type):
      
      try:
          inter = Interface
          frame_type = ether_type
          
          sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
          sock.bind((inter , frame_type))
      
          return sock
      except KeyboardInterrupt:
          print('\n')
      except Exception as exc:
          print(exc)
       
def recv_send():
    try:
     
      if_index = socket.if_nameindex()
            
      for id_if in if_index:
           
           Interface_database = {} 
           
           ID = id_if[0]
           IF = id_if[1]
           
           Interface_database[f'Index {ID}'] = f'Interface {IF}'
           
           if IF.startswith('e'):
              Interface_name = IF
              Ether_type = socket.ETHERTYPE_IP
              
              sock = packet_socket(Interface_name , Ether_type)
              if sock is not None:
                 with open('RECEIVING_IPV4_PACKET.txt' , 'wb') as recv_file:
                      

                         recv_file.write(b'IPv4 Packet\n')
                         recv_file.write(b"f''{'*' * 15}''" )
                         recv_file.write(b'\n')
                         
                         while True:
                                    raw_data = sock.recv(1024)
                                    decoded_data = raw_data.decode(errors='ignore')
                                    n_bytes = recv_file.write(raw_data)          
                                    print(f'Sent [{n_bytes}] bytes to file')
           
    except KeyboardInterrupt:
                 print('\n')
    except Exception as exc:
                 print(exc) 


recv_send() 
      
      
      
      

