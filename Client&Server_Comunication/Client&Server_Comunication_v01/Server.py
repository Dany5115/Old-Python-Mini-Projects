import socket
import threading

s = socket.socket()          
print ("Socket successfully created")
  
# reserve a port on your computer (it can be anything)
port = 12345                

# listen to requests coming from any computers on the network 
s.bind(('', port))         
print ("socket binded to %s" %(port)) 
  
# put the socket into listening mode 
s.listen(5)      
print ("socket is listening") 

while True: 
  
   # Establish connection with client. 
   c, addr = s.accept()      
   print ('Got connection from', addr) 

   while True:
      # Functions:
      # get msg
      def GETs():
         print (c.recv(1024).decode('utf-8'))
      getThreads = threading.Thread(target=GETs)
      
      # send msg  
      def SENDs():
         c.send(input().encode('utf-8'))
      sendThreads = threading.Thread(target=SENDs)
      # Start threads:
      getThreads.start()
      sendThreads.start()

   # Close the connection after the second loops finished (add a condition) 
   c.close()
