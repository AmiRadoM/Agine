from Variables import *
import Variables

RB2D = []

class Rigidbody2D():
    def __init__(self, gravity = [0,9.81], mass = 1, useGravity = True):
        self.gravity = gravity  # m/s^2
        self.mass = mass  # kg
        self.velocity = [0,0]  # m/s

        self.useGravity = useGravity  # is the rigidbody affected by gravity

        self.forces = []

    def addForce(self, force = [0,0], type = "force"):
        self.forces.append(Force2D(force,type))

class Force2D():
    def __init__(self, force = [0,0], type = "force"):
        '''
            :arg force: [x,y] is the vector of the force
            :arg type: is the type of the force, which can be: force, acceleration,  impulse, velocityChange
        '''
        self.force = force
        self.type = type


def physics2D():
    # RigidBody2D
    from Attributes import  RB2D
    for object in RB2D:
        rb = object.Rigidbody2D

        #Gravity
        if (rb.useGravity):
                rb.velocity[0] += -rb.gravity[0]
                rb.velocity[1] += -rb.gravity[1]

        for force in rb.forces:
            if(force.type == "force"):
                rb.velocity[0] += (force.force[0]/rb.mass)
                rb.velocity[1] += (force.force[1]/rb.mass)
            elif(force.type == "acceleration"):
                rb.velocity[0] += force.force[0]
                rb.velocity[1] += force.force[1]
            elif(force.type == "impulse"):
                rb.velocity[0] += force.force[0]/rb.mass
                rb.velocity[1] += force.force[1]/rb.mass
                rb.forces.remove(force)
                del force
            elif (force.type == "velocityChange"):
                rb.velocity[0] += force.force[0]
                rb.velocity[1] += force.force[1]
                del force

        # Velocity
        object.x += rb.velocity[0]* Variables.deltaTime
        object.y += rb.velocity[1]* Variables.deltaTime

    clock.tick(fps)

# physicsThread = threading.Thread(target=__Physics2D,args=())
# physicsThread.start()