from .Variables import *
from .Collision2D import *
from .Objects3D import Vector3D



class Force2D():
    def __init__(self, force = Vector3D(0,0), type = "force"):
        '''
            :arg force: [x,y] is the vector of the force
            :arg type: is the type of the force, which can be: force, acceleration,  impulse, velocityChange
        '''
        self.force = force
        self.type = type


def physics2D():
    from .Agine_main import gameDisplay, objects




    for object in objects:
        if (hasattr(object,"Rigidbody2D")):
            rb = object.Rigidbody2D

            #Gravity
            if (rb.useGravity):
                rb.velocity += rb.gravity/10 * Vector3D((gameDisplay.scale / 1000).x,(gameDisplay.scale / 1000).y,1)


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

            collision2D()


            # Velocity
            object.Transform.position += rb.velocity * Variables.deltaTime
