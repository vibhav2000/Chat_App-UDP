# Chat_App-UDP
Here I have created a chat application in python using UDP protocol.

It also utilizes the concept of Socket Programming and Multi-Threading in Python.

WHAT IS UDP?
User Datagram Protocol (UDP) is a Transport Layer protocol. UDP is a part of Internet Protocol suite, referred as UDP/IP suite. Unlike TCP, it is unreliable and connectionless protocol. So, there is no need to establish connection prior to data transfer.
![alt text](https://github.com/vibhav2000/Chat_App-UDP/blob/main/UDP.png?raw=true)

WHAT IS SOCKET PROGRAMMING ?

Socket programming is a way of connecting two nodes on a network to communicate with each other. One socket(node) listens on a particular port at an IP, while other socket reaches out to the other to form a connection. Server forms the listener socket while client reaches out to the server.
They are the real backbones behind web browsing. In simpler terms there is a server and a client.


Let me explain sockets by an example:

`import socket`

`s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)`

Here we made a socket instance and passed it two parameters. The first parameter is AF_INET and the second one is SOCK_DGRAM. AF_INET refers to the address family ipv4. The SOCK_DGRAM means UDP is connection less protocol.
Now we can connect to a server using this "socket".
![alt text](https://github.com/vibhav2000/Chat_App-UDP/blob/main/socketworking.png?raw=true)

WHAT IS THREAD ?

In computing, a process is an instance of a computer program that is being executed. A thread is a single sequential flow of control within a program.

WHAT IS MULTI-THREADING IN PYTHON ?

Multithreading is defined as the ability of a processor to execute multiple threads concurrently.


Let's start by making a workspace to store all our files, which is shared here on GitHub.

So we need to Operating Systems, Windows and Linux (in your case, you can use any).

In socket programming, A server has a bind() method which binds it to a specific ip and port so that it can listen to incoming requests on that ip and port.
socket_family: Defines the family of protocols used as the transport mechanism. It can have either of the two values.
Either AF_UNIX, or

AF_INET (IP version 4 or IPv4).

socket_type: Defines the types of communication between the two end-points. It can have the following values.

SOCK_STREAM (for connection-oriented protocols, e.g., TCP), or
SOCK_DGRAM (for connectionless protocols e.g. UDP).

protocol: We typically leave this field or set this field to zero.

Executing this code is very easy. Just type

`python chat-app-WIN.py` 

And the prgram will run. Similiarly for Linux OS.

In the program, we are taking 2 inputs,
first- the IP Address(of both Windows and Linux OS) and the port number (on which the connection needs to be established).

Below are some of the working proofs- 

![YAY!](https://github.com/vibhav2000/Chat_App-UDP/blob/main/udp-chat1.png?raw=true)

![It WORKS!!](https://github.com/vibhav2000/Chat_App-UDP/blob/main/udp-chat2.png?raw=true)

![YIPEEEE!!](https://github.com/vibhav2000/Chat_App-UDP/blob/main/udp-chat3.png?raw=true)
Here, the connection closes.. Good Bye! 

