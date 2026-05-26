#!/bin/python3
import socket




def socket_fac( inter ):
      try:
            sock = socket.socket(socket.AF_PACKET , socket.SOCK_RAW , socket.htons(0x0003))
            sock.bind((inter , 0))
      
            return sock
      
      except Exception:
            return None

def recv_packet():
      
      
      name_index = socket.if_nameindex()
      interface_store = {}
      
      print("Available inteface") 
      print("`" * 18)
      
      for interface in name_index:
            
            index = interface[0]
            name = interface[1]
            
            interface_store[index] = name
            
            print(f">> [{index}] : [{name}]")
      
      
      try:
        
        answer = int(input("\nInterface: "))
        print('\r')      
 
        if answer in  interface_store and isinstance(answer , int):
           inter = interface_store.get(answer , None)
           
           if inter:
                
                c_sock = socket_fac(inter)

                with open("RECEIVING_ALL_PACKET.txt" , 'w') as packet_file:
                         packet_file.write("ALL_PACKET\n")
                         packet_file.write(f'{"*" * 17}\n' )   
                         
                         while True:
                                data = c_sock.recv(102422)
                                decode_data = data.decode(errors='ignore')
                                n_bytes = packet_file.write(decode_data)
                                print(f'Sent [{n_bytes}] to file')

        else:
             print("Invalid argument")      
                 
      except ValueError:
             print("[ choose from the intefaces above by their index eg , 1 for localhost(lo)  ]")
             
      except Exception as exc:
             print(exc)        

      except KeyboardInterrupt:
             ...
              
recv_packet()
