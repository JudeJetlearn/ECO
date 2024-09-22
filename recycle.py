import pgzrun
import random

WIDTH = 700
HEIGHT = 500

items = ["bag","battery","botwater","chips"]
finalitems = []
startlev = 1
endlev = 6
newact = []


def draw():
    screen.blit("eco", (0 , 0))
    if len(newact)>0:
        for i in newact:
         i.draw()

def create_item(noex):
    global newact
    options = getops(noex)
    print(options)
    newact = createAct(options)
    layout(newact)

def getops(noex):
    itemsinlev = ["paperbag"]

    for i in range(noex):
      item = random.choice(items)
      itemsinlev.append(item)
    return itemsinlev

def createAct(options):
    actors = []
    for i in options:
        a = Actor(i)
        actors.append(a)
    return actors

def layout(newact):
    gaps = len(newact)+1
    gapsize = WIDTH/gaps
    newact.shuffle()
    for index,item in enumerate(newact):
        item.x = gapsize*(index+1)





create_item(5)

pgzrun.go()