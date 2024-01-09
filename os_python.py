#print(dir(str))
#print(help(str))

import os
#print(help(os))
#print(os.getcwd())
#print(help(open))


def writeData():
    data = '\nHello world!'
    with open('random.txt' 'a') as f:
        f.write(data)
        f.close()

def openFile():
    #with is like a while loop
    with open("random.txt", "r") as f:
        data = f.read()
        print(data)
        f.close()

if __name__ == "__main__":
    writeData()
    openFile()