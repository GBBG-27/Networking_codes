#!/bin/python3
import socket , selectors


try: 

     host_n = input('Hostname: ')
     port_n = int(input('Port: '))

except ValueError:
    
    host_n = None
    port_n = None
    print('\n[ Invalid argument ]\n')
    
except Exception as exc:
    
     host_n = None
     port_n = None
     print(exc)
     

def sock_obj( host , port ):

       try:                   
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM )
            sock.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR , 1)
            sock.bind(( host , port )) 
            sock.listen(3)
       
            conn , addr = sock.accept()
            print(f'\n[ Static connection made for  [ {addr[0]} : {addr[1]} ]')
       
            return conn
       except Exception as exc:
            print(f'\n[ {exc} ]')
            return None 
            
def selector_process():
       
  sock = sock_obj( host_n , port_n )
  
  if sock is not None: 
       
      select_obj = selectors.DefaultSelector()
      select_obj.register(sock , selectors.EVENT_READ , data='read')
  
      r_data = {}
      gaurd_1 = True
      while gaurd_1:
              
                 poll_obj = select_obj.select()
      
                 for key , event in poll_obj:
           
                       if event & selectors.EVENT_READ and key.data =='read':
              
                          conn = key.fileobj
                          
                          try:
                               _data  =  conn.recv(1024)
                          
                               if _data:
                
                                      de_data = _data.decode()
                                      r_data['data_1'] = de_data
                                      print(f'\n>> Received: {de_data}') 
                                      select_obj.modify(conn , selectors.EVENT_WRITE , data='write')
               
                               else:
                                      print('\n[ Disconnected ]')
                                      raise KeyboardInterrupt
                                 
                          except Exception as exc:
                                      print(exc)

                                               
                       elif event & selectors.EVENT_WRITE  and key.data=='write':
                             gaurd_2 = True
                           
                             if gaurd_2:
                          
                                 try:
                                                            
                                      conn = key.fileobj
                                      _data = r_data['data_1']
                                      conn.send(_data.encode()) 
                                      print('>> Data echoed back')
                                      select_obj.modify(conn , selectors.EVENT_READ , data='read')  
                             
                                 except  BrokenPipeError:
                                  
                                              print('\n[ Disconnected ]') 
                                              gaurd_1 = False
                                              gaurd_2 = False
  else:                  
       print('\n[ SOCK_FAILED ]')      
try:
     selector_process()
except KeyboardInterrupt:
     print('\n')   
    
