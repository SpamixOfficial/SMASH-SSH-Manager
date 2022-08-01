import time
from random import randint
rainbowmode = False
from colorama import Fore
import sys
import os

color = Fore.RED

if True:
    checkrainbowmode = 'rainbowmode=true'
    settingsfile = open("settings.txt", 'r+')
    readfilesize = 'settings.txt'
    if os.stat(readfilesize).st_size == 0:
        with settingsfile as f:
            f.write("rainbowmode=false")
    if checkrainbowmode in settingsfile:
        rainbowmode = True

    settingsfile.close()


string1 = """
                         ______                     
 _________        .---\"\"\"      \"\"\"---.              
:______.-':      :  .--------------.  :             
| ______  |      | :                : |             
|:______B:|      | |  Little Error: | |             
|:______B:|      | |                | |             
|:______B:|      | |       Bai      | |             
|         |      | |                | |             
|:_____:  |      | |        :C      | |             
|    ==   |      | :                : |             
|       O |      :  '--------------'  :             
|       o |      :'---...______...---'              
|       o |-._.-i___/'             \._              
|'-.____o_|   '-.   '-...______...-'  `-._          
:_________:      `.____________________   `-.___.-. 
                 .'.eeeeeeeeeeeeeeeeee.'.      :___:
              .'.eeeeeeeeeeeeeeeeeeeeee.'.         
             :____________________________:
"""
string2 = """
 ___________
||   UwU   ||            _______
||   Hewo  ||           | _____ |
||    :D   ||           ||_____||
||_________||           |  ___  |
|  + + + +  |           | |___| |
    _|_|_   \           |       |
   (_____)   \          |       |
              \    ___  |       |
       ______  \__/   \_|       |
      |   _  |      _/  |       |
      |  ( ) |     /    |_______|
      |___|__|    /         
           \_____/
"""
def settings():
    print(Fore.RED + "$ ", end='')
    for x in "rainbowmode(y/n)":
        rainbow()
        print(color + x, end='')
    print('\r')
    print(Fore.RED + "$ " + Fore.YELLOW + "settings")

def rainbow():
    number = randint(1, 16)
    global color
    if number == 1:
        color = Fore.RED
    elif number == 2:
        color = Fore.YELLOW
    elif number == 3:
        color = Fore.CYAN
    elif number == 4:
        color = Fore.BLACK
    elif number == 5:
        color = Fore.GREEN
    elif number == 6:
        color = Fore.WHITE
    elif number == 7:
        color = Fore.MAGENTA
    elif number == 8:
        color = Fore.BLUE
    elif number == 9:
        color = Fore.LIGHTRED_EX
    elif number == 10:
        color = Fore.LIGHTYELLOW_EX
    elif number == 11:
        color = Fore.LIGHTCYAN_EX
    elif number == 12:
        color = Fore.LIGHTBLACK_EX
    elif number == 13:
        color = Fore.LIGHTGREEN_EX
    elif number == 14:
        color = Fore.LIGHTWHITE_EX
    elif number == 15:
        color = Fore.LIGHTMAGENTA_EX
    elif number == 16:
        color = Fore.LIGHTBLUE_EX

def artwork(type):
    global rainbowmode
    if type == "open":
        if rainbowmode == True:
            for char in string2:
                rainbow()
                print(color + char, end='')
                time.sleep(0.003)
        else:
            for char in string2:
                print(Fore.CYAN + char, end='')
                time.sleep(0.003)
    elif type == "bye":
        if rainbowmode == True:
            for char in string1:
                rainbow()
                print(color + char, end='')
                time.sleep(0.003)
        else:
            for char in string1:
                print(Fore.RED + char, end='')
                time.sleep(0.003)

def cmdlist():
    print(Fore.GREEN + "\"quit\"")
    print(Fore.YELLOW + "Quits the script!")
    print(Fore.GREEN + "\"list\"")
    print(Fore.YELLOW + "Displays all the commands!")
    print(Fore.GREEN + "\"settings\"")
    print(Fore.YELLOW + "Displays all the settings available!")

def quit(type):

    if type == "now":
        sys.exit(0)
    else:
        artwork(type="bye")
        sys.exit(0)

def ssh(type):
    if type == "help":
        print("prints help")
    if type == "create":
        print("creates new ssh")

commands = {
    'list':             cmdlist,
    'settings':         settings
}





artwork(type="open")
if rainbowmode == True:
    for x in range (3):
        rainbow()
        print(color, "Loading", end='')
        time.sleep(0.5)
        for x in range(3):
            rainbow()
            print(color + ".", end='')
            time.sleep(0.5)
        print(end="\r")
else:
    for x in range (3):
        print(Fore.CYAN, "Loading", end='')
        time.sleep(0.5)
        for x in range(3):
            print(Fore.CYAN + ".", end='')
            time.sleep(0.5)
        print(end="\r")

if rainbowmode == True:
    print('\n')
    for char in "Done!":
        rainbow()
        print(color + char, end='')
else:
    print(Fore.CYAN, "\nDone!")

time.sleep(0.5)
if rainbowmode == True:
    print('\n')
    for char in "Commands please! ->":
        rainbow()
        print(color + char, end='')
    print("\n")
else:
    print(Fore.RED + "\nCommands please! -> ")
while True:
    if True:
        cmd = input(Fore.RED + "$")

        _cmd = commands.get(cmd)

    if _cmd:
        _cmd()

    elif cmd == "rainbowmode y":
        rainbowmode = True
        lines = []
        with open(r"settings.txt", 'r') as fp:
            lines = fp.readlines()


        with open(r"settings.txt", 'w') as fp:
            for number, line in enumerate(lines):
                if number not in [0]:
                    fp.write(line)
            fp.write("rainbowmode=true")
        print("Rainbowmode has been turned on!")

    elif cmd == "rainbowmode n":
        rainbowmode = False
        lines = []
        with open(r"settings.txt", 'r') as fp:
            lines = fp.readlines()


        with open(r"settings.txt", 'w') as fp:
            for number, line in enumerate(lines):
                if number not in [0]:
                    fp.write(line)
            fp.write("rainbowmode=false")
        print("Rainbowmode has been turned off!")
    elif cmd == "quit":
        quit(type="")
    elif cmd == "quit -n":
        quit(type="now")
    elif cmd == "ssh -h":
        ssh(type="help")
    elif cmd == "ssh -c":
        ssh(type="create")
    else:
        print("That ain't a command!")

