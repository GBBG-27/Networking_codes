#!/bin/python3
import socket
# This is a simple python script acting as a client that 
# connects to servers.You will be prompt to enter a hostname
# which could be an ip address or domain name,then a port number,
# the script will connect to the address and wait for you to 
# send data


def client_socket(): # function to return the socket object 
             try: # catching errors and exception

                    host = input("Hostname: ") # hostname
                    port = int(input("Port: ")) # port 

                    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # socket object
                    client_socket.connect(( host , port )) # connect to address
              
                    return client_socket # return the socket object
             
             except Exception as exc: # catching exception
                    
                    return None
              

def process(): # function to send and receive data
            try: # catching errors and exception
             
                    sock = client_socket() # the socket object 
                    
                    if sock: # cross-check if socket object was obtained
                             print('\n[ Connected ]\r')
                             while True: # loop to send and receive data
                      
                                     data = input("\n>> ") # data to be sent
                                     if len(data) != 0: # check whether length of data is not zero
                                     
                                             encode_data = data.encode() # encode data
                                             sock.send(encode_data) # send data
                                     else: # executes if length of data is zero
                                             print('\n[ Improper request ]')
                                             break
                                             
                                             
                                     recv_data = sock.recv(1024) # receive data
                                     
                                     if len(recv_data) != 0: # check whether received data is not zero 
                                          
                                            decode_recv_data = recv_data.decode() # decode received data
                                            print(f"Responds: {decode_recv_data}") # print received data out 
                                     
                                     else:
                                           print("\n[ Server disconnected]")
                                           break     
                    else:
                           
                           print('\n[Connection failed]')
            
            except BrokenPipeError: # catch brokenpipeerror
                    
                    print("\n[ Server disconnected ]")
                           
            except Exception as exc: catch exceptions
                    
                    print(exc)
             
            except KeyboardInterrupt: catch keyboardinterrupt
                    ...              
                           
                           
                           
process() # run the function


















