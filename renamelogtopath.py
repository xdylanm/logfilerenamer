#!/usr/bin/python3

import os

basepath = os.getcwd()
print("Looking for logs starting in {}".format(basepath))

for root, dir, files in os.walk(basepath):
    for file in files:
        if file.endswith(".log"):
            splitroot = os.path.split(root)[-1]
            if splitroot:
                oldfile = os.path.join(root,file)
                newfile = os.path.join(root,splitroot+".log")
                print("Renaming log file {} to {}".format(os.path.relpath(oldfile,basepath),os.path.relpath(newfile,basepath)))
                os.rename(oldfile,newfile)
    
