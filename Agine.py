from Agine import *
import sys

def update():
    pass


#Start
cam = GameObject()
cam.Camera = Camera()

a = GameObject()
a.Square = Square()

#Init
updateFunctions.append(update)
Main()