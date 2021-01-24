from Agine_main import *
import threading

def update():
    while not crashed.get("crashed"):
        speed = 500
        if(KeyPressed["d"]):
            s1.Rigidbody2D.velocity = Vector2D(speed , s1.Rigidbody2D.velocity.y)
        if (KeyPressed["a"]):
            s1.Rigidbody2D.velocity = Vector2D(-speed , s1.Rigidbody2D.velocity.y)
        if(not KeyPressed["d"] and not KeyPressed["a"]):
            s1.Rigidbody2D.velocity = Vector2D(0 , s1.Rigidbody2D.velocity.y)

        if(KeyDown["space"]):
            s1.Rigidbody2D.velocity = Vector2D(0, 500)

        pass



        


def start():

    s1.addAttr("BoxCollider")
    s2.addAttr("BoxCollider")
    s3.addAttr("BoxCollider")
    s4.addAttr("BoxCollider")
    s5.addAttr("BoxCollider")


    s1.BoxCollider.isVisible = True
    s2.BoxCollider.isVisible = True
    s3.BoxCollider.isVisible = True
    s4.BoxCollider.isVisible = True
    s5.BoxCollider.isVisible = True

    s5.BoxCollider.isTrigger = True

    s1.addAttr("Rigidbody2D")



    pass

#Variables


s1 = Circle(position=Vector2D(-50,0), radius= 25)
#
s2 = Square(position= Vector2D(-100,-200), scale = Vector2D(100,100))
s3 = Square(position= Vector2D(0,-200), scale = Vector2D(100,100))
s4 = Square(position= Vector2D(100,-200), scale = Vector2D(100,100))
s5 = Square(position= Vector2D(200,-200), scale = Vector2D(100,100))

# l1 = Line(startPoint= Vector2D(-500,500))

start()

#threading
updateThread = threading.Thread(target=update,args=())
updateThread.start()
Main()