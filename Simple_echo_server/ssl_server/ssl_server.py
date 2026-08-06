#!/bin/python3
import socket , ssl



def sock_object(host , port):
      try:
           
           sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
           sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
           sock.bind((host , port))
           sock.listen(2)
      
           return sock
  
      except Exception as exc:
           
           print(f'\nError:  [{exc}]\n')
           return None

def ssl_con():
     
     
     ssl_cxt = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
     return ssl_cxt
      


def ssl_process():
     
     try:
         
            host = input('>> Hostname: ')
            port = int(input('>> Port: '))
     
     except Exception as exc:
           
           host = None
           port = None
         
           print(f'\nError:  [{exc}]\n')
     try:      
     
      if host and port:      
             
        sock = sock_object( host , port )
        
        if sock:
    
           ssl_context = ssl_con()
     
       
           with ssl_context.wrap_socket(sock , server_side=True) as secured_socket:
              
                    connection , address = secured_socket.accept()
                    print(f'\n[ {address[0]}:{address[1]} ] connected\n')
                    
                    while True:
                              try:
                                    
                                    data_recv = connection.recv(1024)
                                    decode_data_recv = data_recv.decode()
                                    print(f'\n>> Received: {decode_data_recv}')
              
                                    nb = connection.send(data_recv)
                                    print(f'>> Echoed {nb} bytes back')
                               
                              except ssl.SSLEOFError as exc:
                                    
                                    print(f'Error:  [{exc}]')
                                    break
                                      
        else:
               
               print('[ Socket failed ]\n')     
      else:
            
            print('[ Server failed ]\n') 
     
     except Exception as exc:
             
             print(f'Error: [{exc}]')      
try:

     ssl_process()

except KeyboardInterrupt:
     
     print('\n')
