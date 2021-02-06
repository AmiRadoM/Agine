from Agine import *
import sys

def update():
    pass


#Start
cam = GameObject()
cam.addAttr("Camera")

a = GameObject()
a.addAttr("Square")

#Init
updateFunctions.append(update)
Main()