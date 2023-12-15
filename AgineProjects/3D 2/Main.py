import math

from Agine import *

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

    cube.Transform.rotation += Vector3D.One() * 1 * Variables.deltaTime

    pass


#Start
cam = GameObject()
cam.Camera = Camera()


cube = GameObject()
cube.Cube = Cube()
cube.Transform.position.z += 10
cube.Cube.TextureLoad("./Amir.png")



#Init
updateFunctions.append(update)
Main()