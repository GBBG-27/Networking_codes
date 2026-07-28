#!/bin/python3
import socket 
import selectors

# This is a simple script that connects to servers 
# and send and receive data.It connects to the address
# you give,a hostname and a port number,when a connection is
# successful data can then be sent.When the other peer
# disconnects,you will be notified when you send data




def host_port():
      
      """
         This function returns the required arguments,
         the hostname and port number that the client 
         will connect to then send and receive data.If 
         an error occurs 'None' will be returned
      """
      try: # catching errors and exceptions
          
           host = input('>> Hostname: ') # Hostname
           port = int(input('>> Port: ')) # Port number 
           
           return host , port # return value
      except ValueError as exc:
     
           print('\n[ Invalid arguments ] ') 
           return None , None
     
      except Exception as exc:
           return None , None

def sock_obj():
      
       """
          This function returns the socket object [ connection object ]
          that connects to the server
       """
      
       host , port = host_port() # host and port
       try: # catching errors and exceptions
             
             if host and port: # condition to verify if host and port is available
       
                 client_sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM) # socket object
                 client_sock.connect((host , port)) # connect to host and port 
      
                 return client_sock # return socket object
       
             else:
                     return None
       
       except Exception as exc:
                     print(f'\n Error : [ {exc}]')
                     
                     return None            
       
               
def monitoring_process():
      
      """
         This function is responsible for monitoring,it monitors 
         the socket object created by the previouse function for 
         input [ reading data ] and output [ writing data ].
      """
       
      sock = sock_obj() # get the socket object
       
      if sock: # check if socket was obtained
                
                  selector = selectors.DefaultSelector() # object for monitoring
                  selector.register(sock , selectors.EVENT_WRITE , data='write') # attach the socket to the monitoring object with only writing privilages
       
                  data = {} # storing the data to be sent
       
                  gaurd = True
        
                  while gaurd: # Loop for the process
                  
                            select_obj = selector.select() # return objects for monitoring
                  
                            for key , event in select_obj: # loop through the previvous object for objects for monitoring and information 

                                    # Condition to verify the socket object,privilege given and extra information
                                    if key.fileobj == sock and event & selectors.EVENT_WRITE and key.data == 'write':
                                             try: # catching errors and exception
                                                   
                                                   sock = key.fileobj # socket object
                                                   send_data = input('\n>> ') # Data to send
                          
                                                   if send_data: # condition to verify if data was valid 
                                
                                                           encode_send_data = send_data.encode() # encode data to bytes
                                                           data['data_1'] = encode_send_data # store the data
                                  
                                                           n_bytes = sock.send(encode_send_data) # send the data
                                                           print(f'>> [ {n_bytes} ] bytes sent ') # print number of bytes sent
                             
                                                           selector.modify(sock , selectors.EVENT_READ , data='read') # change the settings for the socket object
            
                                                   else:            
                                     
                                                            print('\n[ Closed connection ]')   
                                                            gaurd = False
                                            
                                             except BrokenPipeError:
                                                          
                                                          print('[ Disconnected ]')                  
                                                          gaurd = False
                                                          
                                             except Exception as exc:
                                                         
                                                          print(f'Error : [ {exc} ]')
                                                          gaurd = False                  
                                                              
                                    # verify the socket object,privilege given and extra information
                                    elif key.fileobj == sock and event & selectors.EVENT_READ and key.data == 'read':
                                          
                                          sock = key.fileobj # socket object 
                                          try: # catching erors and exception
                                                
                                                recv_data = sock.recv(1024) # receive data
                                            
                                                if recv_data: # verify received data
                           
                                                               decode_recv_data = recv_data.decode() # decode the received data
                                                               print(f'\n{decode_recv_data}') # print received data out 
                                                               selector.modify(sock , selectors.EVENT_WRITE , data='write') # change the settings for the socket object 
                            
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
      monitoring_process()  # Run the function
except KeyboardInterrupt:
      print('\n')                      
                           
                           
                           
                              
                                                 
