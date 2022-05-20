import time
from termcolor import colored
from inventory import getinventory, addtoinventory
import first_scene


def UTactv():
    starttime = time.time()
    talkcount = first_scene.talkcount
    # vars used in different scenes to break out of loop
    while True:
        x = input('>').lower()
        currtime = time.time()
        if currtime - starttime > 30 and first_scene.firstsceneevent == True:
            first_scene.phoneEventTrig = True  # trigger phone event
            first_scene.firstsceneevent = False
            break
        elif x in ['talk', 'speak']:
            talkcount += 1
            if talkcount == 1:
                print(colored('You just talked to yourself.', "cyan"))
            if talkcount == 2:
                print(colored("You did it again.", "cyan"))
            if talkcount == 3:
                print(colored("You know my game has other features right?", "cyan"))
            if talkcount == 4:
                print(colored("I'm done entertaining you", "cyan"))
            if talkcount >= 5 and talkcount < 10:
                print(colored("...", "cyan"))
            if talkcount == 10:
                print(
                    colored("fine. you're persistent. here. take this gold coin.", "yellow"))
                addtoinventory("-gold coin")
        elif x in ['inventory', 'open inventory', 'inv']:
            print(colored(getinventory(), "green"))

            continue
        elif x == 'look' or x == 'see' or x == 'look around' and first_scene.firstsceneevent == True:
            first_scene.printscene()
            continue

        elif x in ["get phone", "use phone", "look at phone", "phone", "take phone"]:

            print(colored("A casual phone. Not the best, but it works.", 'blue'))
            phoneEventTrig = True
            break
        elif x in ['mommy', 'mom', 'mommy?', 'mom?']:
            print(colored("daddy?", 'yellow'))
        elif x in ['daddy', 'dad', 'daddy?', 'dad?']:
            print(colored("mommy?", 'yellow'))
        elif x in ['ok', 'ok.', 'okay']:
            print(colored("yes", 'blue'))
        elif x in ['yes', 'yes.', 'yeah', 'yeah.', 'yep', 'yep.', 'yea', 'yea.', 'ye', 'ye.']:
            print(colored("no", 'blue'))
        elif x in ['no', 'nah', 'no.', 'nah.']:
            print(colored("yes", 'blue'))
        elif x in ['uh', 'uhh', 'uhhh', 'uhhhh']:
            print(colored("um", 'blue'))
        elif x in ['um', 'umm', 'ummm', 'ummmm']:
            print(colored("uhh", 'blue'))
        else:
            print(colored("error lol", "blue"))
            continue
