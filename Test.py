from Agine import *


def update():
    speed = 5
    
    if(KeyPressed["d"]):
        s1.Rigidbody2D.velocity = Vector3D(speed , s1.Rigidbody2D.velocity.y)
    if (KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector3D(-speed , s1.Rigidbody2D.velocity.y)
    if(not KeyPressed["d"] and not KeyPressed["a"]):
        s1.Rigidbody2D.velocity = Vector3D(0 , s1.Rigidbody2D.velocity.y)

    if(KeyDown["space"]):
        s1.Rigidbody2D.velocity = Vector3D(s1.Rigidbody2D.velocity.x, 15)


    pass



        


#Start

cam1 = GameObject()
cam1.addAttr("Camera")

ground = GameObject()
ground.addAttr("Square")

s1 = GameObject(name="Player")
s1.addAttr("Sprite")
s1.Sprite.imagePath = "./assets/Character.png"

t= GameObject()
t.addAttr("Text")
t.Transform.position = Vector3D(0, 100)

s1.Transform.position = Vector3D(0, 1)


def f():
    print("Clicked!!")

b = GameObject()
b.addAttr("Button")
b.Button.onClick.append(f)
b.addAttr("Square")
b.Transform.position = Vector3D(1.5,0)


ground.addAttr("BoxCollider")

s1.addAttr("BoxCollider")

s1.BoxCollider.localScale.x = 0.5
ground.BoxCollider.isVisible = True
s1.BoxCollider.isVisible = True


s1.addAttr("Rigidbody2D")
# s1.Rigidbody2D.gravity = Vector3D(0, -0.1)








#Init
updateFunctions.append(update)
Main()