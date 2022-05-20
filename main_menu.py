import keyboard
import os
from termcolor import cprint, colored


def displaymainmenu():

    cprint("Continue\t    New Game\n     (Type 'c' or 'n')",
           'blue', attrs=['blink'])

    while True:
        if keyboard.read_key() == 'n':
            x = input()
            os.system('cls')
            return 'new game'

        elif keyboard.read_key() == 'c':
            return 'continue'
