from Agine_main import *
import threading

def update():
    speed = 500
    if(KeyPressed["d"]):
        s1.Rigidbody2D.velocity = Vector2D(speed , s1.Rigidbody2D.velocity.y)
    if (KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector2D(-speed , s1.Rigidbody2D.velocity.y)
    if(not KeyPressed["d"] and not KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector2D(0 , s1.Rigidbody2D.velocity.y)

    if(KeyDown["space"]):
        s1.Rigidbody2D.velocity = Vector2D(s1.Rigidbody2D.velocity.x, 2000)

    pass



        


def start():


    ground.addAttr("BoxCollider")

    s1.addAttr("BoxCollider")
    s2.addAttr("BoxCollider")
    # s3.addAttr("BoxCollider")
    # s4.addAttr("BoxCollider")







    s1.addAttr("Rigidbody2D")
    s2.addAttr("Rigidbody2D")
    # s3.addAttr("Rigidbody2D")
    # s4.addAttr("Rigidbody2D")



    #s1.Rigidbody2D.addForce(Vector2D(0,-10), "force")


    #s3.Rigidbody2D.gravity = Vector2D(0,-1)

    pass

#Variables

ground = Square(position= Vector2D(-100,-200), scale = Vector2D(500,100))


s1 = Square(name= "controlled",position=Vector2D(-100,-100), scale= Vector2D(50,50))
s2 = Square(name= "notControlled",position=Vector2D(-51,200), scale= Vector2D(50,50))
# s3 = Square(name= "controlled",position=Vector2D(-0,-100), scale= Vector2D(50,50))
# s4 = Square(name= "notControlled",position= Vector2D(51,-100), scale = Vector2D(50,50))

start()

#threading
updateFunctions.append(update)
Main()