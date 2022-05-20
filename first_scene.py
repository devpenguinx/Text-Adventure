from time import sleep
from tracemalloc import start
from termcolor import colored
import os
import keyboard
import time
from inventory import getinventory, addtoinventory
from userterminal import UTactv

firstsceneevent = True
phoneEventTrig = False
talkcount = 0


def main():

    os.system('cls')  # clear screen

    op1 = "You find yourself walking through an empty school hallway late at night.\n"
    for char in op1:
        sleep(0.01)
        print(colored(char, 'blue'), end='', flush=True)

    # place terminal here

    UTactv()
    if phoneEventTrig:
        op2 = "You feel your phone buzzing in your pocket...\n"

        for char in op2:
            sleep(0.01)
            print(colored(char, 'red'), end='', flush=True)

        while True:
            x = input('>').lower()
            if x == 'inventory' or x == 'open inventory':
                print(colored(getinventory(), "green"))

            elif x in ["get phone", "use phone", "look at phone", "phone", "take phone"]:
                phoneintro()


count = 0  # counter for password tries
lockscr = 'Enter lockscreen password: '


def phoneintro():
    global lockscr
    global count

    os.system('cls')
    for char in lockscr:
        sleep(0.05)
        print(colored(char, 'blue'), end='', flush=True)
    passw = input('').lower()
    count += 1
    if passw == '42':
        print('Unlocked')
    elif passw == 'password':
        for char in 'haha.. nice try':
            sleep(0.05)
            print(colored(char, 'red'), end='', flush=True)

        sleep(2)
        phoneintro()
    elif passw == '69':
        for char in 'nice... but no.':
            sleep(0.05)
            print(colored(char, 'red'), end='', flush=True)
        sleep(2)
        phoneintro()
    elif passw in ['boobies', 'boobs', 'titties', 'tits']:
        print(colored("ayo? those mommy milkers huh. unfortunately no.", "blue"))
        sleep(2)
        phoneintro()
    elif count > 5:
        lockscr = '\nHint: The answer to life, the universe, and everything\nEnter lockscreen password:'
        phoneintro()

    else:
        phoneintro()


def printscene():
    print(colored('The hallway is completely empty. Except for a trashcan and vending machine. \nThe vending machine humms quietly and lights up the dark hallway.', 'blue'))
