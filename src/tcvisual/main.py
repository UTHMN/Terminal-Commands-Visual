import time
import sys
import os
import winsound as ws
import turtle
import pyperclip
import requests
import pywhatkit

global start_time
global iNav
global querySuccess
global wsapp
global wnum
iNav: bool = False
querySuccess: bool = False
wsapp: str = ""
wnum: str = ""
start_time = time.time()

def shibe():
    url = "http://shibe.online/api/shibes"
    r = requests.get(url)
    rContent = r.content
    print(rContent)

def cat():
    url = "http://shibe.online/api/cats"
    r = requests.get(url)
    rContent = r.content
    print(rContent)

def bird():
    url = "http://shibe.online/api/birds"
    r = requests.get(url)
    rContent = r.content
    print(rContent)

def circle():
    turtle.circle(50)
    turtle.exitonclick()
    print("DO NOT REOPEN")

def square():
    turtle.shape("square")
    turtle.exitonclick()
    print("DO NOT REOPEN")

def printer():
    i = input("query: ")
    print(i)

def shutdown():
    ws.PlaySound("SystemExit", ws.SND_ASYNC)
    time.sleep(2.5)
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()

def benchmark():
    fps = (1.0 / (time.time() - start_time)) * 100
    print("FPS: ", round(fps, 2))
    print(f"Cpu Cores: {os.cpu_count()}")
    print(f"Operating System: {os.name}")

def help():
    print("STANDALONE COMMANDS:")
    print("help                 Displays list of commands")
    print("benchmark            Runs a benchmarking application")
    print("exit                 Exits the terminal")
    print("print                Prints the given query")
    print("Clear                Clear the terminal")
    print("PATH TOOLSET:")
    print("path --edit          Edits a given file")
    print("path --open          Opens a given file")
    print("path --print         Prints a given file (to the printer)")
    print("path --properties    Finds properties of a file")
    print("path --find          Finds if given file exists")
    print("path --remove        Removes a file at a given path")
    print("path --list          Lists the contents of a directory at a given path")
    print("path --add           Adds a file at a given directory")
    print("path --current       Displays the current path you are running")
    print("path --size          Displays the size of a path in megabytes")
    print("path --nav           Lets you navigate to a certain path and copies it to the clipboard")
    print("path --read          Prints the contents of a file (to the terminal)")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def whatsapp():
    # sending message to me
    # using pywhatkit
    wnum = input("Receiver's phone number: ")
    wsapp = input("Message to send: ")
    pywhatkit.sendwhatmsg(f"{wnum}",
                          f"{wsapp}",
                          12,
                          00)
    print("Successfully Sent!")

def pathread():
    f = open(f"{input('file: ')}", 'r')
    file_contents = f.read()
    print("=====================")
    print(file_contents)
    input("press {enter} to close")
    f.close()
    os.system('cls' if os.name == 'nt' else 'clear')

def pathnav():
    print(os.listdir("C:/"))
    tPath = "C:/"
    temp = tPath
    iNav = True
    while iNav:
        Cpath = input("path: ")
        if Cpath == "exit":
            tPath = temp + Cpath
            temp = tPath + "/"
            pyperclip.copy(f"{tPath}")
            print("successfully copied to clipboard, remove the 'exit' string")
            iNav = False
        else:
            tPath = temp + Cpath
            print(os.listdir(tPath))
            temp = tPath + "/"

def pathsize():
    pathSize = input("Directory path to be read: ")
    if os.path.exists(f"{pathSize}"):
        peth = os.path.getsize(f'{pathSize}') / 100
        print(f'{pathSize} is {peth} gigabytes')
    else:
        print("Error: path does not exist")

def pathcurrent():
    if os.path.exists(f"{os.getcwd()}"):
        print(f'Current directory: {os.getcwd()}')
    else:
        print("Error: file does not exist")

def pathadd():
    pathAdd = input("Directory path to be created: ")
    os.makedirs(f"{pathAdd}")

def pathlist():
    pathList = input("Directory path to be listed: ")
    if os.path.exists(f"{pathList}"):
        print(os.listdir(f"{pathList}"))
    else:
        print("Error: file does not exist")

def pathremove():
    pathRemove = input("Directory path to be removed: ")
    if os.path.exists(f"{pathRemove}"):
        os.remove(f"{pathRemove}")
    else:
        print("Error: directory does not exist")

def pathopen():
    path = input("path: ")
    if os.path.exists(f"{path}"):
        os.startfile(f"{path}", "open")
    else:
        print("Error: file does not exist")

def pathprint():
    path = input("path: ")
    if os.path.exists(f"{path}"):
        os.startfile(f"{path}", "print")
    else:
        print("Error: file does not exist")

def pathedit():
    path = input("path: ")
    if os.path.exists(f"{path}"):
        os.startfile(f"{path}", "edit")
    else:
        print("Error: path does not exist")

def pathprops():
    path = input("path: ")
    if os.path.exists(f"{path}"):
        os.startfile(f"{path}", "properties")
    else:
        print("Error: path does not exist")

def pathfind():
    path = input("path: ")
    os.startfile(f"{path}", "find")