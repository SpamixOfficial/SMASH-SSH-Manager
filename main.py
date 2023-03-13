import time, sys, os, json
from random import randint
rainbowmode = False
from colorama import Fore

color = Fore.RED

with open("settings.json") as f:
    data = json.load(f)
rainbowmode = data['rainbow']
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
    color_map = {
    1: Fore.RED,
    2: Fore.YELLOW,
    3: Fore.CYAN,
    4: Fore.BLACK,
    5: Fore.GREEN,
    6: Fore.WHITE,
    7: Fore.MAGENTA,
    8: Fore.BLUE,
    9: Fore.LIGHTRED_EX,
    10: Fore.LIGHTYELLOW_EX,
    11: Fore.LIGHTCYAN_EX,
    12: Fore.LIGHTBLACK_EX,
    13: Fore.LIGHTGREEN_EX,
    14: Fore.LIGHTWHITE_EX,
    15: Fore.LIGHTMAGENTA_EX,
    16: Fore.LIGHTBLUE_EX
    }

    color = color_map.get(number)

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
        data['rainbow'] = True
        #lines = []
        #with open(r"settings.txt", 'r') as fp:
        #    lines = fp.readlines()


        #with open(r"settings.txt", 'w') as fp:
        #    for number, line in enumerate(lines):
        #        if number not in [0]:
        #            fp.write(line)
        #    fp.write("rainbowmode=true")
        with open("settings.json") as f:
            json.dump(data, f, indent=4)
        print("Rainbowmode has been turned on!")

    elif cmd == "rainbowmode n":
        rainbowmode = False
        data['rainbow'] = False
        #lines = []
        #with open(r"settings.txt", 'r') as fp:
        #    lines = fp.readlines()


        #with open(r"settings.txt", 'w') as fp:
        #    for number, line in enumerate(lines):
        #        if number not in [0]:
        #            fp.write(line)
        #    fp.write("rainbowmode=false")
        with open("settings.json", "wb") as f:
            json.dump(data, f, indent=4)
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
        ssh(type="help")

