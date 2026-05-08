#!/bin/python3
import socket
# This is a simple script that intercepts data being 
# transmitted on a network.When data is transmitted on 
# a network while the script is running,raw data or 
# packet will be captured and written to a file. 

def packet_socket(Interface , ether_type):
         
         """
             The socket object that will be used for the
             interception will be created from this function
         """
         
         
         try: # catching errors and exceptions 
               inter = Interface # interface to use
               frame_type = ether_type # ether_type to use

               # creating the socket then bind an interface to it      
               sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
               sock.bind((inter , frame_type))
           
               return sock # return the socket object 
         except Exception as exc:
                  print(f'Error_A : {exc}')      
        
def recv_write():
            """
               This function is responsible for intercepting raw packet 
               and writing the raw packet to a file
            """
            # retrieving the system's interfaces
            interface_name_index = socket.if_nameindex()

            interface_store = {} # storing the interfaces
            index_store = [] # storing the index of the interfaces 

            print('Available Interface')
            print(f"{'`' * 19}")

            # loop through the system interfaces 
            for inters in interface_name_index:

                  inter_index = inters[0] # interface name
                  inter_name = inters[1] # interface index
                  interface_store[inter_index] = inter_name # send the interface to interface store   

                  # print the available intefaces out   
                  print(f">>> [{inter_index}]:[{inter_name}]")

            # loop through the interface to retrieve the index and store it 
            for num in interface_store:    
                   index_store.append(num)


            print("\nInteface")
            print(f'{"`" * 8}')
            
            try: # catching errors and exceptions
                   # This answer will choose the interface to intercept 
                   answer = int(input(">>> ")) 
            except ValueError:
                   answer = None
            except KeyboardInterrupt:
                   answer = None
                   
            try: # catching errors and exception 
              # verify the answer with a simple condition
              if answer in index_store and answer <= len(index_store):

                interface = interface_store[answer] # get the interface
                ether_type = socket.ETHERTYPE_IP # ether_type to use
                sock = packet_socket(interface , ether_type) # retrieve the socket object

                # the file raw packet will be written to         
                with open("RECEIVING_IPV4_PACKET.txt" , 'a') as packet_file:

                        # write some extra data to the file
                        packet_file.write('\nIPv4 data\n') 
                        packet_file.write(f"{'*' * 11}\n")

                        if sock is not None: # a conditional statement 
                               print('\n')
                               # loop to capture raw data and write it to a file continueously 
                               while True:
                                      try: # catching errors and exception
                                          recv_data = sock.recv(1024) # receive data 
                                          decode_data = recv_data.decode(errors='ignore') # decode data
                                          n_bytes = packet_file.write(decode_data) # write data
                                          print(f"Sent [{n_bytes}] to file") # print out
                                      except KeyboardInterrupt:
                                          break     
                        else:
                              print('\n')    
              else:
               print('\nInvalid answer')                      
    
            except Exception as exc:
               print(f'Error_B: {exc}')    
               
    
                     
recv_write() # run the code

