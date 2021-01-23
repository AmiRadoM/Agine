from Physics2D import *


RB2D = []  #  RB2D = RigidBody2D
class Rigidbody2D():
    def __init__(self, gravity = [0,9.81], mass = 1, useGravity = True):
        self.gravity = gravity  # m/s^2
        self.mass = mass  # kg
        self.velocity = [0,0]  # m/s

        self.useGravity = useGravity  # is the rigidbody affected by gravity

        self.forces = []

    def addForce(self, force = [0,0], type = "acceleration"):
        self.forces.append(Force2D(force,type))


BC = []  # BC = Box Collider
class BoxCollider():
    def __init__(self, x = 0, y = 0, scale = [0, 0], isVisible = False, isTrigger = False):

        self.x = 0
        self.localX = x
        self.y = 0
        self.localY = y
        self.scale = [0,0]
        self.localScale = scale
        self.isVisible = isVisible
        self.isTrigger = isTrigger

        from Objects2D import Square
        self.square = Square(width=2, color =(0,255,0), isVisible=False)

