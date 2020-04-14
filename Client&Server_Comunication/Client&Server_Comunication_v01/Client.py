import socket
import threading

s = socket.socket()          
  
# Define the port you want to connect 
port = 12345                
  
# connect to the server on local computer (you can change it to the ip address of the computer)
s.connect(('127.0.0.1', port))

while True:

    while True:
        # Functions:
        # send msg
        def SENDc():
            s.send(input().encode('utf-8'))
        sendThreadc = threading.Thread(target=SENDc)
        # get msg
        def GETc():
            print (s.recv(1024).decode('utf-8'))
        getThreadc = threading.Thread(target=GETc)
        # Start threads:
        getThreadc.start()
        sendThreadc.start()

    # close the connection (with the condition that finishes the second loop)
    s.close()
