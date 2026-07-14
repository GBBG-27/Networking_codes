#!/bin/python3
import socket , selectors

# This is a simple echo server that bounces data 
# sent to it,when a connection is made with data 
# sent,it will printed out and echoed back.When the 
# script starts,you will be prompt to enter a hostname;
# it can be an ip address or a domain name,next you
# will enter the port number for the server to listen on.
# What makes this different from my other servers is that
# it utilizes a different method in sending and receiving the data.
# This time the server will be monitored for input and output,when data 
# is coming,the server will be alert and then handle the process with a
# different method,same thing applies when data is ready to be sent.


try: # catching errors and exceptions

     host_n = input('Hostname: ') # Hostname
     port_n = int(input('Port: ')) # Port number

except ValueError:
    
    host_n = None
    port_n = None
    print('\n[ Invalid argument ]\n')
    
except Exception as exc:
    
     host_n = None
     port_n = None
     print(exc)
     

def sock_obj( host , port ): 
       """
          This function is respondsible for creating the 
          socket object that will be monitored for input and output
          then return it
       """

       try:
            sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM ) # socket object
            sock.bind(( host , port )) # bind to the host and port
            sock.listen(3) # listen for connection that can wait
       
            conn , addr = sock.accept() # return a socket to send and recv data on a connection and also return the address of that connection
            print(f'\n[ Static connection made for  [ {addr[0]} : {addr[1]} ]')
       
            return conn
       except Exception as exc:
            print(f'\n[ {exc} ]')
            return None 
            
def selector_process(): 

  """
     This function will perform all the process,it monitors input output
     and send and receive data
  """
     
  sock = sock_obj( host_n , port_n ) # get the socket object
  
  if sock is not None: # condition to verify if the socket object was obtained

      
      select_obj = selectors.DefaultSelector() # object for monitoring
      select_obj.register(sock , selectors.EVENT_READ , data='read') # register the socket object then monitor only input then an extra data for verification
  
      r_data = {}
      gaurd_1 = True
      while gaurd_1: # loop to monitor while sending and receiving 
              
                 poll_obj = select_obj.select() # return two objects for the monitoring
      
                 for key , event in poll_obj: 
                       
                       # verify some conditions,which event the socket was registered with and the extra data            
                       if event & selectors.EVENT_READ and key.data =='read': # This is for reading ( receiving data )
              
                          conn = key.fileobj # get the socket object of the connected peer
                          
                          try:
                               _data  =  conn.recv(1024) # receive data
                          
                               if _data: # if data was received
                
                                      de_data = _data.decode() # decode data
                                      r_data['data_1'] = de_data # store data
                                      print(f'\n>> Received: {de_data}') 
                                      select_obj.modify(conn , selectors.EVENT_WRITE , data='write') # configure the monitoring setting
               
                               else:
                                      print('\n[ Disconnected ]')
                                      raise KeyboardInterrupt
                                 
                          except Exception as exc:
                                      print(exc)

                       # verify some conditions,which event the socket was registered with and the extra data                        
                       elif event & selectors.EVENT_WRITE  and key.data=='write': # This is for writing( sending data )
                             gaurd_2 = True
                           
                             if gaurd_2:
                          
                                 try: # catching errors and exceptions
                                                            
                                      conn = key.fileobj # socket object 
                                      _data = r_data['data_1'] # get the received data
                                      conn.send(_data.encode()) # encode and send it
                                      print('>> Data echoed back')
                                      select_obj.modify(conn , selectors.EVENT_READ , data='read') # change the monitoring settings
                             
                                 except  BrokenPipeError:
                                  
                                              print('\n[ Disconnected ]') 
                                              gaurd_1 = False
                                              gaurd_2 = False
  else:                  
       print('\n[ SOCK_FAILED ]')      
try:
     selector_process() # call the function
except KeyboardInterrupt:
     print('\n')   
    
