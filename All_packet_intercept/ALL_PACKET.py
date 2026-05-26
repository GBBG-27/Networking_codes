#!/bin/python3
import socket

# This is a simple script that intercept data being 
# transmitted on a network.When data is being transmitted 
# on a network, the script captures the data being transmitted
# and writes it to a file



def socket_fac( inter ):
      """
         The purpose of this function is to create 
         and return the socket object the script will 
         use for the interception
      """
      try: # catching errors and exception
            
            sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW , socket.htons(0x0003)) # socket object 
            sock.bind((inter , 0)) # bind the interface with the ether-type
      
            return sock # return the socket object
      
      except Exception:
            # when an exception occurs,the function returns None 
            return None

def recv_packet():
      """
         This function will be respondsible for capturing
         the raw data on the network and continueouselly write it to 
         a file
      """
      
      name_index = socket.if_nameindex() # system interface with their indexs
      interface_store = {} # stores the interface 
      
      print("Available inteface") 
      print("`" * 18)

      # loop through the system inteface and store them 
      for interface in name_index:
            
            index = interface[0] # interface name
            name = interface[1] # interface index
            
            interface_store[index] = name
            
            print(f">> [{index}] : [{name}]") # print the interface out
      
      
      try: # catch errors and exceptions

        # this answer will be used to choose the interface name 
        answer = int(input("\nInterface: "))
        print('\r')      

        # verify if the answer is available 
        if answer in  interface_store:
           inter = interface_store.get(answer , None) # retrieve the desired interface 
           
           if inter: # verify if the interface was retrieved 
                
                c_sock = socket_fac(inter) # retrieve the socket object

                # open a file and write the receivd data to it 
                with open("RECEIVING_ALL_PACKET.txt" , 'w') as packet_file:
                      
                         # write some extra data to the file 
                         packet_file.write("ALL_PACKET\n")
                         packet_file.write(f'{"*" * 17}\n' )   
                         
                         # This loop will capture the raw data and 
                         # continueousely write the data to the file  
                         while True:
                                data = c_sock.recv(102422) # receive data
                                decode_data = data.decode(errors='ignore') # decode data
                                n_bytes = packet_file.write(decode_data) # write data to file
                                print(f'Sent [{n_bytes}] to file') # print it out

        else:
             print("Invalid argument")      
                 
      except ValueError:
             print("[ choose from the intefaces above by their index eg , 1 for localhost(lo)  ]")
             
      except Exception as exc:
             print(exc)        

      except KeyboardInterrupt:
             ...
              
recv_packet() # run the function
