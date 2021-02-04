from .Variables import *
from .Collision2D import *
from .Objects2D import Vector2D



class Force2D():
    def __init__(self, force = Vector2D(0,0), type = "force"):
        '''
            :arg force: [x,y] is the vector of the force
            :arg type: is the type of the force, which can be: force, acceleration,  impulse, velocityChange
        '''
        self.force = force
        self.type = type


def physics2D():
    from .Attributes import  rigidbody2d
    from .Agine_main import gameDisplay




    for object in rigidbody2d:
        rb = object.Rigidbody2D

        #Gravity
        if (rb.useGravity):

            rb.velocity += rb.gravity * (gameDisplay.scale / 1000)


        for force in rb.forces:
            if(force.type == "force"):
                rb.velocity += force.force/rb.mass
            elif(force.type == "acceleration"):
                rb.velocity += force.force
            elif(force.type == "impulse"):
                rb.velocity += force.force/rb.mass
                rb.forces.remove(force)
                del force
            elif (force.type == "velocityChange"):
                rb.velocity += force.force
                rb.forces.remove(force)
                del force

        # Collision
        collision2D(object)


        # Velocity
        print(Variables.deltaTime)
        object.Transform2D.position += rb.velocity * Variables.deltaTime
