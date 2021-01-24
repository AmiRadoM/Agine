from Objects2D import Vector2D

RB2D = []  #  RB2D = RigidBody2D
class Rigidbody2D():
    def __init__(self, gravity = Vector2D(0,-9.81), mass = 1, useGravity = True):
        self.gravity = gravity  # m/s^2
        self.mass = mass  # kg
        self.velocity = Vector2D(0,0)  # m/s

        self.useGravity = useGravity  # is the rigidbody affected by gravity

        self.forces = []

    def addForce(self, force = Vector2D(0,0), type = "acceleration"):
        from Physics2D import Force2D

        self.forces.append(Force2D(force,type))


BC = []  # BC = Box Collider
class BoxCollider():
    def __init__(self, position = Vector2D(0,0), scale = Vector2D(0,0), isVisible = False, isTrigger = False):

        self.position = Vector2D(0,0)
        self.localPosition = position
        self.scale = Vector2D(0,0)
        self.localScale = scale
        self.isVisible = isVisible
        self.isTrigger = isTrigger

        from Objects2D import Square
        self.square = Square(width=2, color =(0,255,0), isVisible=False)

