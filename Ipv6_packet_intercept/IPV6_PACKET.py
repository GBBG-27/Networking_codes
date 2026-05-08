#!/bin/python3
import socket 



def interception_operation():        
                                                                                                                                                          
         all_inter = socket.if_nameindex()
         inter_store = {}
         
         print("Available Interfaces")
         print("`" * 20 )
 
         for sys_inter in all_inter:
                                                                                                                                                                
               index = sys_inter[0]                                                                                                                                          
               name = sys_inter[1]                                                                                                                                         
               
               inter_store[index] = name 
               print(f">> [{index}] : [{name}]")                                                                                                                                         
                                                                                                                                                        
         print('Interface')
         print(f'{"`" * 9}\n')
         
         try:                                                                                                                                      
               ans = int(input(">> "))
         except ValueError:
               ans  = None         
         except KeyboardInterrupt:
               ans = None                                                                                                                                     
         
         
         if ans is not None and ans in inter_store:
                         
             interface = inter_store[ans]
             ethertype = socket.ETHERTYPE_IPV6
             
             sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
             sock.bind(( interface , ethertype ))      
             
             with open("RECEIVING_IPV6_PACKET.txt" , 'a') as packet_file:
                      
                      packet_file.write("IPV6 PACKET\n")
                      packet_file.write(f'{"*" * 19}\n')
                      
                      print("\n[ Wait for data to be transmitted through the network interface  ]")
                      print('\n')
                      try:
                      
                           while True:
                           
                                 data_recv = sock.recv(1024)
                                 decode_data = data_recv.decode(errors='ignore')
                                 n_bytes = packet_file.write(decode_data) 
                                 print(f"Sent {n_bytes} to [file]")
                      
                      except BrokenPipeError as exc:
                                 print(exc)
                      
                      except KeyboardInterrupt:
                                 print("\n")                      
                                          
         else:
                print("[ Choose from the interfaces above eg 1 or 2 ]")
         
         
         
                  
interception_operation()                                                                                                                                               
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
                                                                                                                                                        
