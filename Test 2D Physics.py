from Agine import *


def update():
    speed = 5
    
    if(KeyPressed["d"]):
        s1.Rigidbody2D.velocity = Vector2D(speed , s1.Rigidbody2D.velocity.y)
    if (KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector2D(-speed , s1.Rigidbody2D.velocity.y)
    if(not KeyPressed["d"] and not KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector2D(0 , s1.Rigidbody2D.velocity.y)

    if(KeyDown["space"]):
        s1.Rigidbody2D.velocity = Vector2D(s1.Rigidbody2D.velocity.x, 15)


    # cam1.Transform2D.position = s1.Transform2D.position
    pass



        


#Start

cam1 = GameObject()
cam1.addAttr("Camera")

ground = GameObject()
ground.addAttr("Square")

s1 = GameObject(name="Player")
s1.addAttr("Sprite")
s1.Sprite.imagePath = "character.png"

t= GameObject()
t.addAttr("Text")
t.Transform2D.position = Vector2D(0, 100)

s1.Transform2D.position = Vector2D(0, 1)


ground.addAttr("BoxCollider")

s1.addAttr("BoxCollider")

s1.BoxCollider.localScale.x = 0.5
ground.BoxCollider.isVisible = True
s1.BoxCollider.isVisible = True


s1.addAttr("Rigidbody2D")
s1.Rigidbody2D.gravity = Vector2D(0, -0.1)








#Init
updateFunctions.append(update)
Main()