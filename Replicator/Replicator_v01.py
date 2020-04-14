# What this does is that it keeps creating a .txt file that keeps duplicating itself with another name.

import os
import time

file = "1"

while 1 > 0:
    f= open(file + ".txt","a")
    time.sleep(1) # Amount of time in sec
    file += "1"
