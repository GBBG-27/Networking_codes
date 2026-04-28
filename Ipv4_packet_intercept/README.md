# Description
This is a simple python script that intercept raw data being

transmitted on a network interface and simply write the data 
 
to a file.The script was designed to only intercept 
 
Internet Protocol version 4 packet.The 
 
ARP packet being transimtted is encoded and encrypted
 
so the script decodes it with utf-8,if the data cannot 
 
be decoded,in the file,a question mark is replaced and on the
 
terminal 'whitespace character' is replaced and also it's 
 
encrypted so you won't be able to read , but sometimes,some
 
messages are not.

## Steps 
##### -You must have python installed on the machine(On Unix based computers python is pre-installed).
##### -The script will require root privileges because it will access system resources.
##### -Open the terminal and run "sudo python IPV4_PACKET.py" , authenticate for the script to start working.
##### -Whenever data is written to the file it's printed out.
