## Description

This is a simple server written in  python that

echoes back data sent to it.When the script starts 

you will be prompt to enter an `IP ADDRESS` and a 

`PORT` number,after you give the necessary details the script 

will start to listen on the address given.When a connection is made,

the address of the connection will be printed out,it then waits

for data from the other end (client).When the client sends data,

it will be printed out and then send it back while printing 

the number of bytes sent.Data can be sent and received continuously.

The server will run forever unless manually stopped.With a connection made,

data can be exchanged,when the client closes its connection or aborts,it will be

printed out that that particular address closed the connection,here the server does

not close,it just closes that specific address and still listens for more connections.


## Usage

#### - First download the script  [ Download the repo ]
#### - Open a terminal within the directory containing the script
#### - Run the script [type python Server.py in the terminal]
#### - You will be prompt to enter the hostname [Type a legit ip and press enter]
#### - You will be asked the second time to enter the port number [Enter the port and press enter]
#### - The server starts listening on the given address 
#### - When a connection is made,a message will be printed out that an address made a connection
#### - With the connection,data can be exchanged
#### - Whenever the client sends data it will be printed out
#### - After that,the server echoes back the data while printing the number of bytes sent
#### - When the client closes it's connection,the server will print that that particular client closed it's connection
#### - At this point the server does not close,it still listens for more connecton

###### Thank You
