from Agine_main import *
import threading


def update():
    while not crashed.get("crashed"):
        l1.endPoint = mousePos.toList()

        if(LineVsSqr(l1,s1,c1)):
            print(True)
        pass
        


def start():

    s1.addAttr("BoxCollider")
    s1.addAttr("Rigidbody2D")
    s1.BoxCollider.isVisible = True
    s1.Rigidbody2D.useGravity = False
    # s1.Rigidbody2D.addForce([500,0], 'impulse')
    
    

    pass

#Variables


s1 = Square(x = 0)

l1 = Line(startPoint=[-500,500],width = 3)

c1 = Circle(radius=10, color=(255,0,0), isVisible=False)




start()

#threading
updateThread = threading.Thread(target=update,args=())
updateThread.start()
Main()