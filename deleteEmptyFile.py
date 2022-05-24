import re
import glob
import os

vaultDir = '/Users/jfuentes/Notes/Notes/JRoam/'
files = os.listdir(vaultDir)

for file in files:
    # print(file)
    # check if size of file is 0
    # print(file)
    # print(os.stat(vaultDir + file).st_size)
    if os.stat(vaultDir + file).st_size <= 3:
        os.remove(vaultDir + file)
        print(file)