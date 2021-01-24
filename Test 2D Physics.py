from Agine_main import *
import threading

def update():
    while not crashed.get("crashed"):

        pass



        


def start():

    s1.addAttr("BoxCollider")
    s2.addAttr("BoxCollider")

    s1.BoxCollider.isVisible = True
    s2.BoxCollider.isVisible = True


    s1.addAttr("Rigidbody2D")
    s1.Rigidbody2D.useGravity = True

    s1.Rigidbody2D.addForce(Vector2D(.5,9), 'force')

    pass

#Variables


s1 = Square(position=Vector2D(-50,0), scale= Vector2D(50,50))

s2 = Square(position= Vector2D(0,-400), scale = Vector2D(500,200))


start()

#threading
updateThread = threading.Thread(target=update,args=())
updateThread.start()
Main()