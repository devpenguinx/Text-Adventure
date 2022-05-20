inventory = ['-a phone', '-car keys']


def getinventory():
    return "Your inventory:\n" + "\n".join(inventory)


def addtoinventory(item):
    inventory.append(item)
