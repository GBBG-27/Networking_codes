#!/bin/python3
import socket 
# This is a simple script that intercept raw packet being
# transmitted within a network.Data is captured on a network 
# and written to a file


def interception_operation():        
         """
            This function is respondsible for the interception process,
            the system interfaces with their index are retrieved
            and are prompt to the user,you choose your desired interface
            and the interception proceed.This function creates a socket,
            bind the inteface and the ethertype to it.When data is captured,
            the function will write the data to a file and print out the number
            of bytes sent
         """                                                                                                                                                 
         
         all_inter = socket.if_nameindex() # computer's interfaces
         inter_store = {} # stores the interfaces
         
         print("Available Interfaces")
         print("`" * 20 )

         # loop through the interfaces,print it out and 
         # store it 
         for sys_inter in all_inter:
                                                                                                                                                                
               index = sys_inter[0] # interface index                                                                                                                                         
               name = sys_inter[1]  # interface name                                                                                                                                       
               
               inter_store[index] = name # store the interface 
               print(f">> [{index}] : [{name}]") # print it out                                                                                                                                        
                                                                                                                                                        
         print('Interface')
         print(f'{"`" * 9}\n')
         
         try: # catching errors and exceptions                                                                                                                                      
               ans = int(input(">> ")) # answer to use for the interface  
         except ValueError:
               ans  = None         
         except KeyboardInterrupt:
               ans = None                                                                                                                                     
         
         # verify if the answer true and valid
         if ans is not None and ans in inter_store:
                         
             interface = inter_store[ans] # retrieve the interface
             ethertype = socket.ETHERTYPE_IPV6 # ethertype to use

             # a socket is created and the interface and ethertype is bind to it 
             sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
             sock.bind(( interface , ethertype ))      

             # the file that will receive the raw packet intercepted in the network 
             with open("RECEIVING_IPV6_PACKET.txt" , 'a') as packet_file:

                      # write extra data to the file
                      packet_file.write("IPV6 PACKET\n")
                      packet_file.write(f'{"*" * 19}\n')
                      
                      print("\n[ Wait for data to be transmitted through the network interface  ]")
                      print('\n')
                      try: # catching errors and exceptions

                           # this loop is responsible for receiving the raw packet, 
                           # write it to the file while printing the number of bytes 
                           # sent continueously
                           while True:
                           
                                 data_recv = sock.recv(1024) # receive data
                                 decode_data = data_recv.decode(errors='ignore') # decode data
                                 n_bytes = packet_file.write(decode_data) # write data
                                 print(f"Sent {n_bytes} to [file]") # print number of bytes out
                      
                      except BrokenPipeError as exc:
                                 print(exc)
                      
                      except KeyboardInterrupt:
                                 print("\n")                      
                                          
         else:
                print("[ Choose from the interfaces above eg 1 or 2 ]")
         
         
         
                  
interception_operation()  # run the function                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
