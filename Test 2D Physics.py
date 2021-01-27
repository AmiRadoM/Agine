from Agine import *
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
    #
    s1.addAttr("BoxCollider")
    # s2.addAttr("BoxCollider")
    #
    #
    s1.BoxCollider.localScale.x = -25
    #
    #
    #
    s1.addAttr("Rigidbody2D")
    # s2.addAttr("Rigidbody2D")

    pass

#Variables

camera = object2D().addAttr("Camera")

ground = Square(position= Vector2D(-0,-0), scale = Vector2D(100,100))

l1 = Line(endPoint=Vector2D(0,100))

s1 = Sprite(image= "Character.png",name= "controlled",position=Vector2D(-100,200), scale= Vector2D(50,50))
# s2 = Square(name= "notControlled",position=Vector2D(-50,200), scale= Vector2D(50,50))
# s3 = Square(name= "controlled",position=Vector2D(-0,-100), scale= Vector2D(50,50))
# s4 = Square(name= "notControlled",position= Vector2D(51,-100), scale = Vector2D(50,50))


start()

#threading
updateFunctions.append(update)
Main()