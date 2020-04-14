# What this does is that it keeps creating a .txt file that keeps duplicating itself with another name.
# New feature(A): custom file path added!
# New feature(B): replicate renamed in hashes!

import os
import time
import os.path
import getpass

file = "1"
username = "\\" + str(getpass.getuser())
path = 'C:\\Users' + username # A:Your desired path to replicate :)

while 1 > 0:
   f= open(os.path.join(path, str((file,).__hash__()) + ".txt"),"a") # B:This is where all the hashing happens!
   time.sleep(1) # Amount of time in sec
   file += "1"
