#!/bin/python3
import socket


def packet_socket(Interface , ether_type):
         try: 
               inter = Interface
               frame_type = ether_type

               sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
               sock.bind((inter , frame_type))
           
               return sock
         except Exception as exc:
                  print(f'Error_A : {exc}')      
        
def recv_write():

            interface_name_index = socket.if_nameindex()

            interface_store = {}
            index_store = []

            print('Available Interface')
            print(f"{'`' * 19}")

            for inters in interface_name_index:

                  inter_index = inters[0]
                  inter_name = inters[1]
                  interface_store[inter_index] = inter_name

                  print(f">>> [{inter_index}]:[{inter_name}]")

            for num in interface_store:    
                   index_store.append(num)


            print("\nInteface")
            print(f'{"`" * 8}')
            #print(interface_store)
            #print(index_store)

            try:
                   answer = int(input(">>> "))
            except ValueError:
                   answer = None
            except KeyboardInterrupt:
                   answer = None
                   
            try: 
              if answer in index_store and answer <= len(index_store):

                interface = interface_store[answer]
                ether_type = socket.ETHERTYPE_IP 
                sock = packet_socket(interface , ether_type)

                with open("RECEIVING_IPV4_PACKET.txt" , 'a') as packet_file:

                        packet_file.write('IPv4 data\n')
                        packet_file.write(f"{'*' * 11}\n")

                        if sock is not None:
                               print('\n')
                               while True:
                                      try:
                                          recv_data = sock.recv(1024)
                                          decode_data = recv_data.decode(errors='ignore')
                                          n_bytes = packet_file.write(decode_data)
                                          print(f"Sent [{n_bytes}] to file")
                                      except KeyboardInterrupt:
                                          break     
                        else:
                              pass    
              else:
               print('\nInvalid answer')                      

            except Exception as exc:
               print(f'Error_B: {exc}')    

recv_write()
