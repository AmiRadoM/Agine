import math

from Agine import *

class Pole():
    def __init__(self):
        self.t = 0
        pass

def update():
    if (KeyPressed["space"]):
        cam.Transform.position.y += 1 * Variables.deltaTime
    if (KeyPressed["lshift"]):
        cam.Transform.position.y -= 1 * Variables.deltaTime
    if (KeyPressed["w"]):
        cam.Transform.position += cam.Transform.Forward() * 1 * Variables.deltaTime
    if (KeyPressed["s"]):
        cam.Transform.position -= cam.Transform.Forward() * 1 * Variables.deltaTime
    if (KeyPressed["a"]):
        cam.Transform.position -= cam.Transform.Right() * 1 * Variables.deltaTime
    if (KeyPressed["d"]):
        cam.Transform.position += cam.Transform.Right() * 1 * Variables.deltaTime
    if (KeyPressed["left"]):
        cam.Transform.rotation.y -= 1 * Variables.deltaTime
    if (KeyPressed["right"]):
        cam.Transform.rotation.y += 1 * Variables.deltaTime

    for p in poles:
        p.Pole.t += 1

        p.Transform.scale.y = math.sin(p.Pole.t - Vector2D(p.Transform.position.x, p.Transform.position.z).Distance()) + 1

    pass


#Start
cam = GameObject()
cam.Camera = Camera()

w = 3
h = 3

poles = []

for i in range(0,w):
    for j in range(0,h):
        meshCube = GameObject()
        meshCube.Cube = Cube()
        meshCube.Transform.position = Vector3D(i - w/2 +  0.5, 0, j - h/2)
        meshCube.Pole = Pole()
        poles.append(meshCube)



#Init
updateFunctions.append(update)
Main()