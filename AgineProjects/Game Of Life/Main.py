import copy
from Agine import *

class Stats(Attribute):
    def __init__(self):
        self.active = False

def click(gObject):
    gObject.Stats.active = not gObject.Stats.active

def clickHackMap(hackMap):
    hackMap["newSqr"].Stats.active = True

def update():
    global speedCounter
    global pause

    print(str(speedCounter) + " || " + str(1/Variables.deltaTime))

    newArr = copy.deepcopy(arr)

    if (not pause):
        speedCounter+=Variables.deltaTime

    for i in range(0, y, 1):
        for j in range(0, x, 1):
            if (arr[j][i].Stats.active == True):
                arr[j][i].Square.color = (255, 255, 255)
            else:
                arr[j][i].Square.color = (0, 0, 0)

    if speedCounter >= speed:
        speedCounter = 0

        for i in range(0, y, 1):
            for j in range(0, x, 1):

                counter = (int(arr[j-1][i-1].Stats.active) if j>0 and i>0 else 0) + (int(arr[j][i-1].Stats.active) if i>0 else 0) + (int(arr[j+1][i-1].Stats.active) if j<x-1 and i>0 else 0) + (int(arr[j-1][i].Stats.active) if j>0 else 0) + (int(arr[j+1][i].Stats.active) if j<x-1 else 0) + (int(arr[j-1][i+1].Stats.active) if j>0 and i<y-1 else 0) + (int(arr[j][i+1].Stats.active) if i<y-1 else 0) + (int(arr[j+1][i+1].Stats.active) if j<x-1 and i<y-1 else 0)

                if (arr[j][i].Stats.active == True):

                    if (counter < 2 or counter > 3):
                        newArr[j][i].Stats.active = False
                else:

                    if (counter == 3):
                        newArr[j][i].Stats.active = True

        for i in range(0, y, 1):
            for j in range(0, x, 1):
                arr[j][i].Stats.active = newArr[j][i].Stats.active

    if (KeyDown["space"]):
        pause = not pause

    pass


#Start
x = 20
y = 20
arr = []

speed = 0.3
speedCounter = 0
pause = True

#Squares
for j in range(0,y,1):
    arr.append([])
    for i in range(0,x,1):
        newSqr = GameObject()
        newSqr.Transform.scale = Vector3D(0.2,0.2,1)
        newSqr.addAttr("Square")
        newSqr.addAttr("Button")
        newSqr.Stats = Stats()
        newSqr.Transform.position = Vector3D(-4.9 + j*0.19,4.9 - i*0.19,0)
        arr[j].append(newSqr)
        newSqr.Button.onClick.append(lambda a: click(a))


cam = GameObject()
cam.addAttr("Camera")


#Init
updateFunctions.append(update)
Main()