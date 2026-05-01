#!/bin/python3
import socket

# This is a simple script that intercept a network interface 
# and capture the raw packet being transmitted on the network 
# interface.A socket is bind to a network interface and captures any 
# ARP(Address Resoluiton Protocol) being transmitted on the network



# global variables
INTERFACE = None 
ETHERTYPE = None

def  inter_ether():
  """
       The purpose of this function is to set
       the values of the interface and ethertype
       that the script will use
 
  """
  
  try: # catching exceptions and errors
        name_index = socket.if_nameindex() # return the system's interfaces
        interface_database = {} # stores the interfaces
        interface_index = []   # store the index of the interfaces
 
        # loop through the interfaces
        for inter_info in name_index: 
                
              index = inter_info[0] # interface index
              name = inter_info[1] # interface name
           
              # stores the interface with the index into interface_database
              interface_database[index]  = name 
              # stores the interface index into interface_index
              interface_index.append(index)
      
        print("Available Interfaces")
        print("`" * 20)
        
        # print out available interfaces
        for ind , name  in interface_database.items():
              print(f">> [{ind}] : [{name}]")


        print("\nInterface")
        print('`' * 9)
     
        try:  # catching exceptions and errors 
                  opt = int(input('>> '))
        except ValueError:
                  opt = None
         
        # a conditional statements that verifies the answer 
        # and compares it to interface_index  
        if opt in interface_index and opt is not None: 
                  
                  interface = interface_database[opt] # get the database
                  ether_type = socket.ETHERTYPE_ARP # the ethertype to use
                  
                  # this will modify the global variable 
                  global INTERFACE
                  INTERFACE = interface

                  # this will modify the global variable
                  global ETHERTYPE
                  ETHERTYPE = ether_type              
        else:
                  print("Invalid arguments")
  except KeyboardInterrupt:
                  print('\nKeyboard Interrupted')
  except Exception as exc:
                  print(exc) 

   
inter_ether() # running the function

def recv_and_write():
    """
       The function receives the raw packet and
       write is to a file and print it out everytime 
       data is written to the file

    """
    # catching exceptions and errors
    try:

       # a conditional statement that verifies the interface and ethertype 
       if INTERFACE is not None and ETHERTYPE is not None:
             
             # create the socket object and bind it to the interface and the ethertype
             sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW)
             sock.bind(( INTERFACE , ETHERTYPE ))
             
             # the file that will be use to receive the raw packet 
             with open('RECEIVING_ARP_PACKETS.txt' , 'a') as packet_file:
                
                    packet_file.write("ARP_PACKET\n") # write to the file 
                    packet_file.write(f'{"*" * 10}\n') # write to the file
               
                    print("\n")

                    # a loop to continueously receive data and written to the file
                    while True:
                       
                       # catching exceptions and errors
                       try:    
                             recv_data = sock.recv(1024) # receive data
                             decode_data = recv_data.decode(errors='ignore') # decode data
                             n_bytes = packet_file.write(decode_data) # send data
                             print(f"sent [{n_bytes}] to file") # print number of bytes sent 
                       
                       except BrokenPipeError:
                             print("Peer error") 
                       except Exception as exc:
                             print(exc)

       else:
              pass                   
    
    except KeyboardInterrupt:
              print('Keyboard Interrupted')
       

recv_and_write()  # run the function
