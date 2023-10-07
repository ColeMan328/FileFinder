# Glob test (for use on Linux OS)

import os
import glob

files = glob.glob('/home/**/*', recursive = True) # read all file names on system

look = input('File to find: ') # user input for file to find

stuff = [] # place for all found file locations to be stored

for file in files:
    print(file)     # ensuring all system file names have been read
    if os.path.isfile(file) and (file.endswith(look) == True or os.path.splitext(file)[0] == look): # searching for desired file locations
        stuff.append(file) # storing all found file locations

print(stuff) # printing all found file locations