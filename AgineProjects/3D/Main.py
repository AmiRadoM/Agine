from Agine import *


def update():
    # mesh.Transform.rotation.z += 1 * Variables.deltaTime
    # mesh.Transform.rotation.x += 1 * Variables.deltaTime
    # mesh.Transform.rotation.y += 1 * Variables.deltaTime

    meshCube.Transform.rotation.z += 1 * Variables.deltaTime
    meshCube.Transform.rotation.x += 1 * Variables.deltaTime
    meshCube.Transform.rotation.y += 1 * Variables.deltaTime

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
    pass


#Start
cam = GameObject()
cam.addAttr("Camera")

o1 = GameObject()
o2 = GameObject()
ground = GameObject()

o1.Transform.position.x = 2
o2.Transform.position.x = -2

o1.Transform.position.y = 2
o2.Transform.position.y = 2

ground.Transform.scale.x = 9

# o1.addAttr("Square")
# o2.addAttr("Square")
# ground.addAttr("Square")

o1.addAttr("BoxCollider")
o2.addAttr("BoxCollider")
ground.addAttr("BoxCollider")

o1.addAttr("Rigidbody2D")
o2.addAttr("Rigidbody2D")

o1.Rigidbody2D.velocity.y = 20
o2.Rigidbody2D.velocity.y = 20

o1.Rigidbody2D.mass = 1
o2.Rigidbody2D.mass = 3

meshCube = GameObject()
meshCube.addAttr("Cube")
meshCube.Cube.texture = pygame.image.load("./Amir.png")
meshCube.Transform.position = Vector3D(0,0,5)
mesh = GameObject()
# mesh.addAttr("Mesh")
# mesh.Mesh.LoadFromOBJ("./StarFox.obj")
# mesh.Transform.position.x = 10


#Init
updateFunctions.append(update)
Main()