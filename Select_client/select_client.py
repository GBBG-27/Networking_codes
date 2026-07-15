#!/bin/python3
import socket , selectors





def host_port():
      
      try:
          
           host = input('>> Hostname: ')
           port = int(input('>> Port: '))
           
           return host , port
      except ValueError as exc:
     
           print('\n[ Invalid arguments ] ') 
           return None , None
     
      except Exception as exc:
           return None , None

def sock_obj():
       
       host , port = host_port()
       try:
             
             if host and port:
       
                 client_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
                 client_sock.connect((host , port))
      
                 return client_sock
       
             else:
                     return None
       
       except Exception as exc:
                     print(f'\n Error : [ {exc}]')
                     
                     return None            
       
               
def monitoring_process():
       
       
      sock = sock_obj()
       
      if sock:
                
                  selector = selectors.DefaultSelector()
                  selector.register(sock , selectors.EVENT_WRITE , data='write')
       
                  data = {}
       
                  gaurd = True
        
                  while gaurd:
                  
                            select_obj = selector.select()
                  
                            for key , event in select_obj:
                        
                                    if key.fileobj == sock and event & selectors.EVENT_WRITE and key.data == 'write':
                                             try:
                                                   
                                                   sock = key.fileobj
                                                   send_data = input('\n>> ')
                          
                                                   if send_data: 
                                
                                                           encode_send_data = send_data.encode()
                                                           data['data_1'] = encode_send_data
                                  
                                                           n_bytes = sock.send(encode_send_data)
                                                           print(f'>> [ {n_bytes} ] bytes sent ') 
                             
                                                           selector.modify(sock , selectors.EVENT_READ , data='read')
            
                                                   else:            
                                     
                                                            print('\n[ Closed connection ]')   
                                                            gaurd = False
                                            
                                             except BrokenPipeError:
                                                          
                                                          print('[ Disconnected ]')                  
                                                          gaurd = False
                                                          
                                             except Exception as exc:
                                                         
                                                          print(f'Error : [ {exc} ]')
                                                          gaurd = False                  
                                                              
                         
                                    elif key.fileobj == sock and event & selectors.EVENT_READ and key.data == 'read':
                                          
                                          sock = key.fileobj
                                          try:
                                                
                                                recv_data = sock.recv(1024)
                                            
                                                if recv_data:
                           
                                                               decode_recv_data = recv_data.decode()
                                                               print(f'>> Received: {decode_recv_data}')
                                                               selector.modify(sock , selectors.EVENT_WRITE , data='write')
                           
                                                else:
                                                      
                                                       print('\n[ Connection closed ]')
                                                       gaurd = False
                                                   
                                          except ConnectionError as exc:             
                                                       print(f'Error: [{exc}]')
                                                       gaurd = False
                                          
                                          except Exception as exc:
                                                       print(f'Error: [{exc}]')
                                                       qaurd = False
                                            
      else:
         print('\n[ Operation Failed ]')               

try: 
      monitoring_process() 
except KeyboardInterrupt:
      print('\n')                      
                           
                           
                           
                              
                                                 
