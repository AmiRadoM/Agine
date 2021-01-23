from Agine_main import *
from Variables import *
import threading




def update():
    while not crashed.get("crashed"):
        rotationChange = 0.00001
        #a.rotationx += rotationChange* deltaTime
        #a.rotationy += rotationChange* deltaTime
        #a.rotationz += rotationChange* deltaTime

        speed = 0.002

        #Input
        if(InputKeyboard.get("up")):
            cameraPos[2] += speed * deltaTime
        if (InputKeyboard.get("down")):
            cameraPos[2] -= speed * deltaTime
        if (InputKeyboard.get("left")):
            cameraPos[0] -= speed * deltaTime
        if (InputKeyboard.get("right")):
            cameraPos[0] += speed * deltaTime
        if (InputKeyboard.get("space")):
            cameraPos[1] -= speed * deltaTime
        if (InputKeyboard.get("lshift")):
            cameraPos[1] += speed * deltaTime
        if (InputKeyboard.get("a")):
            pass
        if (InputKeyboard.get("d")):
            pass


if __name__ == "__main__":

    # gameDisplay.bgColor = [255, 255, 255]

    a = Cube3D("name", position=[0,0,50])
    #a = Sphere3D(position=[0,0,50])
    #a = Object3D("axis.obj", position=[3,3,30])
    #a = Object3D("SpaceShip.obj", "A", position=[0,0,50])
    a = Object3D("StarFox.obj", "A", position=[0,0,50])
    #a = Object3D("teapot.obj", position = [0,0,10], rotation = [180,0,0])


    #threading
    updateThread = threading.Thread(target=update,args=())
    updateThread.start()

    checkClose()
