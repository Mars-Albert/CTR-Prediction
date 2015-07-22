__author__ = 'mars'

import time

def block(file,size=65536):
    while True:
        nb = file.read(size)
        if not nb:
           break
        yield nb

def getLineCount(filename):
    with open(filename,"r",encoding="utf-8") as f:
        return sum(line.count("\n") for line in block(f))

if __name__ == "__main__":
    import sys
    import os
    if len(sys.argv) != 2:
        print("error imput argument")
        sys.exit(-1)
    if not os.path.isfile(sys.argv[1]) :
       print(sys.argv + " is not a file")
       sys.exit(-1)
    start_time = time.time()
    print(getLineCount(sys.argv[1]))
    print(time.time() - start_time ,"seconds")