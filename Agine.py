from Agine import *
import sys

def update():
    pass


#Start
#Camera
cam = GameObject()
cam.Camera = Camera()

#Floor
floor = GameObject()
floor.Square = Square()
floor.Transform.scale.x = 5
floor.BoxCollider = BoxCollider()
# floor.Rigidbody2D = Rigidbody2D(useGravity=False)

#Box1
box1 = GameObject()
box1.Transform.position.y = 3
box1.BoxCollider = BoxCollider()
box1.BoxCollider.scale
box1.Square = Square()
box1.Rigidbody2D = Rigidbody2D(mass=10000000)

#Init
updateFunctions.append(update)
Main()