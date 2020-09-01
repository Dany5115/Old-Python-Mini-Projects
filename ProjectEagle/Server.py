from pynput import mouse
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

reset = 6

while True: 
  
    # Establish connection with client. 
    c, addr = s.accept()      
    print ('Got connection from', addr)


    def timer():
        while True:
            global t0
            t0 = reset
            while t0 >= 0:
                t0 = t0 - 1
                time.sleep(1)
            c.send(b"Didn't Move!")

    Thread1 = threading.Thread(target=timer)
    Thread1.start()

    def on_move(x, y):
        global t0
        t0 = reset


    def on_scroll(x, y, dx, dy):
        global t0
        t0 = reset

    with mouse.Listener(on_move=on_move, on_scroll=on_scroll) as listener:
        listener.join()


   
#{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{
    

    Thread1 = threading.Thread(target=timer)
    
    Thread1.start()
#}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}}

    time.sleep(1) # add this to save ur cpu & ram!

   # Close the connection after the second loops finished (add a condition) 
    #c.close() 

# use c.send()