#!/bin/python3
import socket
# This script is designed to intercept raw packet 
# or data being transmitted in a network and write the 
# raw packet to a file . A socket 
# is created and bind to a network interface and the 
# ethernet type


def packet_socket(Interface , ether_type):
         """
            The purpose of this function is to create and
            return the socket object that will be use to intercept 
            the raw packet on the network.
         """
         
         
         try: # catching errors and exceptions
                  
               # Interface to use
               inter = Interface

               # ethertype to use
               frame_type = ether_type

               # the socket object 
               sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
               sock.bind((inter , frame_type))
           
               return sock
         except Exception as exc:
                  print(f'Error_A : {exc}')      
        
def recv_write():

            """
               when the raw packet has been captured,
               this function is responsible for writing all
               data to a file.When data is written to the file,
               it's printed out 
            """

            # The interfaces on the computer with their ids  
            interface_name_index = socket.if_nameindex()

            
            interface_store = {} # stores the network interfaces 
            index_store = [] # stores the index of the interfaces

            print('Available Interface')
            print(f"{'`' * 19}")

            # loop through the network interfaces on the computer 
            for inters in interface_name_index: 
                  
                  inter_index = inters[0] # index of the network interface
                  inter_name = inters[1] # name of the network interface 
                  interface_store[inter_index] = inter_name # store the interface in interface_store 

                  print(f">>> [{inter_index}]:[{inter_name}]")
                     
            # loop and retrieve index of the network interface  
            for num in interface_store:    
                   index_store.append(num)


            print("\nInteface")
            print(f'{"`" * 8}')
            #print(interface_store)
            #print(index_store)

            try: # catching errors and exceptions
                   # this answer will be used futher in the script  
                   answer = int(input(">>> ")) 
            
            except ValueError:
                   answer = None
            except KeyboardInterrupt:
                   answer = None
                   
            try: # catching errors and excepitons

              # verify if the answer the user gave is accurate        
              if answer in index_store and answer <= len(index_store):

                # retrieve the desired interface 
                interface = interface_store[answer]

                # the ethertype to use
                ether_type = socket.ETHERTYPE_IP 

                # retrieve the socket object        
                sock = packet_socket(interface , ether_type)

                # the file the raw packet will be written to  
                with open("RECEIVING_IPV4_PACKET.txt" , 'a') as packet_file:

                        # write some extra data to the file
                        packet_file.write('IPv4 data\n')
                        packet_file.write(f"{'*' * 11}\n")

                        # verify if the socket object was retrieved
                        if sock is not None:
                               print('\n')

                               # this loop will continueouslly capture raw packets
                               # and write them to the file
                               while True:
                                      try: # catch errors and exceptions

                                          # receive the captured packets
                                          recv_data = sock.recv(1024) 

                                          # decode the captured packets
                                          decode_data = recv_data.decode(errors='ignore')

                                          # write the decoded data to the file
                                          n_bytes = packet_file.write(decode_data)

                                          # print it out every time data is written to the file 
                                          print(f"Sent [{n_bytes}] to file")
                                      except KeyboardInterrupt:
                                          break     
                        else:
                              pass    
              else:
               print('\nInvalid answer')                      

            except Exception as exc:
               print(f'Error_B: {exc}')    

recv_write() # run the function
