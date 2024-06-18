import os
import platform

def shutdown():
    if platform.system() == "Windows":
        os.system('shutdown -s')
    elif platform.system() == "MacOS" or platform.system()== "Linux":
        os.system("shutdown -h now")
    else:
        print("OS not supported.")

def restart():
    if platform.system == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "MacOS" or platform.system() == "Linux":
        os.system('reboot now')
    else:
        print("Os not supported.")

command = input("Use \'r\' for restart and \'s\' for shutdown: ").lower()

if command == "r":
    restart()
elif command == "s":
    shutdown()
else:
    print("Wrong letter")