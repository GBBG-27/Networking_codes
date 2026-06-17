#!/bin/python3
import socket




def client_socket(): 
             try:

                    host = input("Hostname: ")
                    port = int(input("Port: "))

                    client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                    client_socket.connect(( host , port ))
                    client_socket
              
                    return client_socket
             
             except Exception as exc:
                    
                    return None
              

def process():  
            try:
             
                    sock = client_socket()
                    
                    if sock:
                     
                             while True:
                      
                                     data = input("\n>> ")
                                     if len(data) != 0: 
                                     
                                             encode_data = data.encode()
                                             sock.send(encode_data)
                                     else:
                                             print('\n[ Improper request ]')
                                             break
                                             
                                             
                                     recv_data = sock.recv(1024)
                                     
                                     if len(recv_data) != 0:
                                          
                                            decode_recv_data = recv_data.decode()
                                            print(f"Responds: {decode_recv_data}")
                                     
                                     else:
                                           print("\n[ Server disconnected]")
                                           break     
                    else:
                           
                           print('\n[Connection failed]')
            
            except BrokenPipeError:
                    
                    print("\n[ Server disconnected ]")
                           
            except Exception as exc:
                    
                    print(exc)
             
            except KeyboardInterrupt:
                    ...              
                           
                           
                           
process()


















