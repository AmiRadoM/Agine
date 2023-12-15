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
        # print(Variables.deltaTime)
        s1.Rigidbody2D.velocity = Vector3D(s1.Rigidbody2D.velocity.x, 100 * Variables.deltaTime)


    pass



        


#Start

cam1 = GameObject()
cam1.Camera = Camera()

ground = GameObject()
ground.Square = Square()

s1 = GameObject(name="Player")
s1.Sprite = Sprite()
s1.Sprite.imagePath = "./assets/Character.png"

t= GameObject()
t.Text = Text()
t.Transform.position = Vector3D(0, 100)

s1.Transform.position = Vector3D(0, 1)


def f():
    print("Clicked!!")

b = GameObject()
b.Button = Button()
b.Button.onClick.append(f)
b.Square = Square()
b.Transform.position = Vector3D(1.5,0)


ground.BoxCollider = BoxCollider()

s1.BoxCollider = BoxCollider()

s1.BoxCollider.localScale.x = 0.5
ground.BoxCollider.isVisible = True
# s1.BoxCollider.isVisible = True


s1.Rigidbody2D = Rigidbody2D()
s1.Rigidbody2D.gravity = Vector3D(0, -2)








#Init
updateFunctions.append(update)
Main()