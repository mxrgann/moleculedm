import socket
import subprocess
import getpass
from time import sleep

username = getpass.getuser()
hostname = socket.gethostname()

#Define WM's and DE's here

#Template:
# TEMPLATE = {"easyname": "TEMPLATE", "hardname": "template-session"}

XFCE4 = {"easyname": "XFCE4", "hardname": "xfce4-session"}
ICEWM = {"easyname": "IceWM", "hardname": "icewm-session" }
GNOME = {"easyname": "GNOME", "hardname": "gnome-session" }
LXQT = {"easyname": "LXQT", "hardname": "lxqt-session" }

#Insert your options here
mainList = [XFCE4, ICEWM, GNOME, LXQT]

namesList = []
hardnamesList = []

def inputInt():
    while True:
        userInput = input().strip()
        if not userInput:
            return ""
            break
        try:
            userInput = int(userInput)
        except ValueError:
           print("Not a valid input (Integers or Blank Inputs only)")
           continue
        return userInput
        break

for i, item in enumerate(mainList):
    namesList.append(item["easyname"])
    hardnamesList.append(item["hardname"])

subprocess.run("clear", shell=True)
print("Welcome to " + hostname + ", " + username + "!" )
print("Select a number to get started!\n")

for i, item in enumerate(namesList, 1):
    print(i, ") " + item, sep = '', end = ' \n')
print ("\n")

selection = inputInt();
subprocess.run("clear", shell=True)

if not selection:
    print("Blank Input, choosing " + namesList[0] + " (first option as default).");
    print(hardnamesList[0])
    sleep(1)
    subprocess.run("clear", shell=True)

else:
    print(namesList[selection - 1] + " selected. Starting now.")
    print(hardnamesList[selection -1])
    sleep(1)
    subprocess.run("clear", shell=True)



