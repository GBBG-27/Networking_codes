#!/bin/python3
import socket 

# This is a simple server that listen for a connection and
# echoes data back to the client.When the script starts,you will 
# have a prompt to enter a hostname and next the port number,after that 
# the server will start listening on the given address.Whenever data 
# is sent from a client,the server will print it out and then 
# echo the data back to the client,the number of bytes sent will be printed out.When 
# a particular client closes it's connection,the server will not close but 
# rather it closes that particular connection and still 
# listen for connection


def server( host , port , n_conn):
      """
         This function will create the socket object that the server will use
         for the server 
      """      
      
      try: # catching errors and exceptions

            # the socket uses the host and port and listens for connection 
            server_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            server_sock.bind((host , port ))
            server_sock.listen(n_conn)
      
            return server_sock # return the socket object

      except Exception as exc:
            print(exc)
            return None
             
def client_connection():
             try: # catching errors and exceptions
                  try: 
                        HOST  = input("Hostname: ") # hostname
                        PORT = int(input("Port: ")) # port 
                        N_CONN = 3 # number of connections that can wait
                  except Exception as exc:
                        HOST = None
                        PORT = None
      
                  if HOST and PORT: # a condition that verifies if the host and port are available
                     
                               socket_object = server( HOST , PORT , N_CONN) # retrieve the socket object

                    
                               if socket_object is not None: # another condition to check if the socket object was retrieved 
                            
                                        print(f"\n<] Server listening on || [{HOST}]:[{PORT}] || [>") 
                                        
                                        while True: # This loop is responsible for running the server continuously even if a client closes it's connection

                                                    # return an  tobjecthat will be used to send and receive data and the address of each connection
                                                    connection , address = socket_object.accept()  

                                                    host = address[0] # hostname 
                                                    port  = address[1] # port address
                                                    print(f"\n[{host}:{port}] made a connection\n")
       
                                                    send_data = '[ connection successful ]\n' 
                                                    encode_send_data = send_data.encode(encoding='utf-8') # encode data
                                                    connection.send(encode_send_data) # send extra data
              
                                                    while True: # loop that will reveive and send data continuously
                                                                  
                                                                  try:      
                                                                          recv_data = connection.recv(102442) # the socket object 
                                                                          

                                                                          if len(recv_data) != 0: # verifies if received data is not None 
                             
                                                                                      decode_recv_data = recv_data.decode(encoding='utf-8') # decode data
                                                                                      print(f">> Client request: {decode_recv_data}")
                   
                                                                                      echoed_data = decode_recv_data.encode(encoding='utf-8') # encode data 
                                                                                      n_bytes = connection.send(echoed_data) # send data
                                                                                      print(F">> [{n_bytes}] bytes sent to client\n")
                                                                                 
                                                                          else:
                                                                                      print(f"[{host}:{port}] connection closed")       
                                                                                      break
                      
                                                                  except Exception:
                                                                  
                                                                                      print(f"[{host}:{port}] connection closed")       
                                                                                      break
                               else:         
                                       print("\n[ Server failed ]")           
                                                     
                  else:
                          print('\n[ Valid address only ]')     
                              
                                             
             except KeyboardInterrupt:
                          print("\r")          
                          
                          
                          

client_connection() # run the funcion

