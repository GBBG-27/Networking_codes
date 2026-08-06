#!/bin/python3
import socket , ssl






def socket_object():
      
      sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)      
      return sock


def ssl_context():
       
      
      context = ssl.create_default_context(purpose=ssl.Purpose.SERVER_AUTH)
      return context


def secure_transfer():
      try:
      
            host = input(">> Hostname: ")
            port = int(input(">> Port: "))
      
      except Exception as exc:
            
            host = None
            port = None
            
            print(f'\nError: [{exc}] ')
            
            
      sock = socket_object()
      ssl_cxt = ssl_context()
      
      try:
       
       if host and port:
         
      
         with ssl_cxt.wrap_socket(sock , server_hostname=host) as secure_sock:
              
              secure_sock.connect((host , port))
              try:  
                   while True:
                              
                              print('\n')
                         
                              data = input('>> Data:  ') 
                         
                              send_data = data.encode()
                              secure_sock.send(send_data)
              
                              data_recv = secure_sock.recv(1024)
                              decode_data_recv = data_recv.decode()
                
                              print(f'>> Received: {decode_data_recv}')
                              
              except BrokenPipeError as exc:
                            
                           print(f'\nError:  [{exc}]\n')
                           
              except KeyboardInterrupt:  
                           
                           print('\n')
       else:
              
              print('\n[ Connection failed ]\n')
      
      except Exception as exc:
             
              print(f'\nError:  [{exc}]\n')     
try:

      secure_transfer()
      
except KeyboardInterrupt:
      print('\n') 
