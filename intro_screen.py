from time import sleep
from termcolor import cprint, colored
from pyfiglet import figlet_format, Figlet
import os
import keyboard

# RETA
# Really awesome text adventure
# Written by Danie van den berg

#f = Figlet(font='starwars')
# print(f.renderText('RETA'))


def printintro():
    cprint(figlet_format("Welcome To"), 'blue')
    cprint(figlet_format('       R A T A'), 'blue', attrs=['bold'])

    str = "\t(really awesome text adventure)"

    for char in str:
        sleep(0.1)

        print(char, end='', flush=True)

    cprint('\n\t    Press enter to start', 'blue', attrs=['blink'])
    while True:

        if keyboard.read_key() == 'enter':
            x = input()
            os.system('cls')
            break
