#!/bin/python3
import socket 



def server( host , port , n_conn):
      try:
            server_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
            server_sock.bind((host , port ))
            server_sock.listen(n_conn)
      
            return server_sock

      except Exception as exc:
   
            return None
             
def client_connection():
             try:
                  try:
                        HOST  = input("Hostname: ")
                        PORT = int(input("Port: "))
                        N_CONN = 3
                  except Exception as exc:
                        HOST = None
                        PORT = None
      
                  if HOST and PORT:
                     
                               socket_object = server( HOST , PORT , N_CONN)

                    
                               if socket_object is not None:
                            
                                        print(f"\n<] Server listening on || [{HOST}]:[{PORT}] || [>") 
                                        
                                        while True:
                                        
                                                    connection , address = socket_object.accept()

                                                    host = address[0]
                                                    port  = address[1]
                                                    print(f"\n[{host}:{port}] made a connection\n	")
       
                                                    send_data = '[ connection successful ]'
                                                    encode_send_data = send_data.encode(encoding='utf-8')
                                                    connection.send(encode_send_data)
           
                                                    data_store = {}
   
                                                    while True:
                                                                  
                                                                  try:      
                                                                          recv_data = connection.recv(102442)
                                                                          

                                                                          if len(recv_data) != 0:
                             
                                                                                      decode_recv_data = recv_data.decode(encoding='utf-8')
                                                                                      print(f">> Client request: {decode_recv_data}")
           
                                                                                      data_store[address[0]] = decode_recv_data
             
                                                                                      echoed_data = decode_recv_data.encode(encoding='utf-8')
                                                                                      n_bytes = connection.send(echoed_data)
                                                                                      print(F">> [{n_bytes}] bytes sent to client\n")
                                                                                 
                                                                          else:
                                                                                      print(f"[{host}:{port}] connection closed")       
                                                                                      break
                      
                                                                  except Exception:
                                                                  
                                                                                      print(f"[{host}:{port}] connection closed")       
                                                                                      break
                               else:         
                                       print("\n[ Invalid argument ]")           
                                                     
                  else:
                          print('\n[ Valid address only ]')     
                              
                                             
             except KeyboardInterrupt:
                          print("\r")          
                          
                          
                          

client_connection()      

