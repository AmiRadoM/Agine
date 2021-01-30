from Agine import *
import threading

def update():
    speed = 800
    if(KeyPressed["d"]):
        s1.Rigidbody2D.velocity = Vector2D(speed , s1.Rigidbody2D.velocity.y)
    if (KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector2D(-speed , s1.Rigidbody2D.velocity.y)
    if(not KeyPressed["d"] and not KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector2D(0 , s1.Rigidbody2D.velocity.y)

    if(KeyDown["space"]):
        s1.Rigidbody2D.velocity = Vector2D(s1.Rigidbody2D.velocity.x, 2000)

    cam1.Transform2D.position = s1.Transform2D.position
    pass



        


def start():

    cam1.addAttr("Camera")

    s1.color = [255,0,0, 100]

    ground.Transform2D.scale = Vector2D(500,500)
    s1.Transform2D.scale = Vector2D(100,100)
    s1.Transform2D.position = Vector2D(0, 350)

    ground.addAttr("Outline")
    ground.Outline.width = Vector2D(3,3)

    s1.addAttr("Outline")
    s1.Outline.color = [0,0,0,100]
    s1.Outline.width = Vector2D(500, 500)

    ground.addAttr("BoxCollider")
    #
    s1.addAttr("BoxCollider")
    # s2.addAttr("BoxCollider")
    #
    #
    s1.BoxCollider.localScale.x = 0.5
    ground.BoxCollider.isVisible = True
    s1.BoxCollider.isVisible = True
    #
    #
    #
    s1.addAttr("Rigidbody2D")
    # s2.addAttr("Rigidbody2D")


    pass

#Variables

cam1 = Object2D()
cam2 = Object2D()

ground = Square()

l1 = Line(endPoint=Vector2D(0,100))

s1 = Sprite(image= "Character.png")


start()

#threading
updateFunctions.append(update)
Main()