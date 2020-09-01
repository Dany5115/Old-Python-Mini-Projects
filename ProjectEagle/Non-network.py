from pynput import mouse
import time
import threading

reset = 6

def timer():
    while True:
        global t0
        t0 = reset
        while t0 >= 0:
            t0 = t0 - 1
            time.sleep(1)
        print("Didn't Move!")

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
