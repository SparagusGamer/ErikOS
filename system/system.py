from ast import While
from logging import fatal
import time
import os
import json

sysopen = False


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


print("Starting system.")
time.sleep(0.8)
cls()
print("Starting system..")
time.sleep(0.8)
cls()
print("Starting system...")
time.sleep(0.8)
cls()
print("Starting system.")
time.sleep(0.8)
cls()
print("Starting system..")
time.sleep(0.8)
cls()
print("Starting system...")
time.sleep(1)
cls()
print("Welcome to ErikOS")
time.sleep(1)
print("Created by SparagusGamer#0001 and Henrok#5020")
time.sleep(1)
print("All rights reserved")
sysopen = True
time.sleep(1)
cls()
print("Please press enter.")
while sysopen == True:
    syscommand = input("")
    Toopen = False
    while Toopen == False:
        with open("users.json", 'r') as f:
            users = json.load(f)
            cls()
        user = input("Username: ")
        cls()
        if str(user) in users:
            passw = input("Password: ")
            cls()
            if users[str(user)] == str(passw):
                Toopen = True
            else:
                print("Wrong password.")
                time.sleep(1.5)
        else:
            print("That user doesn't exist.")
            time.sleep(1.5)
    while Toopen == True:
        def tooopen():
            Toopen = False
            print("Erik!")
            print("Hello, what you want to do today?")
            print("Type list to list available commands and apps.")

            command = input("")
            if command == ("list"):
                cls()
                print("calculator")

            if command == ("calculator"):
                cls()
                print("test")
        tooopen()
