import math

class Attribute():
    pass

class Transform(Attribute):
    def __init__(self):
        from Agine.Objects3D import Vector3D
        self.position = Vector3D.Zero()
        self.scale = Vector3D(1,1,1)
        self.rotation = Vector3D.Zero()

    def Up(self):
        from Agine.Objects3D import Vector3D, Matrix4x4
        return ((Matrix4x4.MakeRotationZ(self.rotation.z) * Matrix4x4.MakeRotationX(self.rotation.x)) * Vector3D.Up()).Normalize()

    def Forward(self):
        from Agine.Objects3D import Vector3D, Matrix4x4
        return ((Matrix4x4.MakeRotationY(self.rotation.y) * Matrix4x4.MakeRotationX(self.rotation.x)) * Vector3D.Forward()).Normalize()

    def Right(self):
        from Agine.Objects3D import Vector3D, Matrix4x4
        return ((Matrix4x4.MakeRotationY(self.rotation.y) * Matrix4x4.MakeRotationZ(self.rotation.z)) * Vector3D.Right()).Normalize()



class Rigidbody2D(Attribute):
    def __init__(self, gravity = None, mass = 1, useGravity = True):
        from Agine.Objects3D import Vector3D
        if (gravity == None):
            self.gravity = Vector3D(0,-0.981,0)  # m/s^2
        else:
            self.gravity = gravity
        self.mass = mass  # kg
        self.velocity = Vector3D(0,0,0)  # m/s

        self.useGravity = useGravity  # is the rigidbody affected by gravity

        self.forces = []

    def addForce(self, force, type = "acceleration"):
        from .Physics2D import Force2D

        self.forces.append(Force2D(force,type))


class BoxCollider(Attribute):
    def __init__(self, isVisible = False, isTrigger = False):
        from Agine.Objects3D import Vector3D
        self.position = Vector3D.Zero()
        self.localPosition = Vector3D.Zero()
        self.scale = Vector3D.Zero()
        self.localScale = Vector3D(1,1,1)
        self.isVisible = isVisible
        self.isTrigger = isTrigger
        self.onTrigger = []
        self.triggered = False


class Camera(Attribute):

    def __init__(self):
        self.Draw = self.__Draw(self)
        self.scale = 5
        self.near = 0.1
        self.far = 1000
        self.fov = 90

    def fovRad(self):
        return 1/math.tan(math.radians(self.fov * 0.5))

    class __Draw():
        def __init__(self, cam):
            self.cam = cam

        def Square(self, position, scale, color, width):
            from .Objects2D import Square
            from .Agine_main import debugObjects,objects, GameObject
            gameObj = GameObject()

            gameObj.Transform.position = position
            gameObj.Transform.scale = scale

            gameObj.Square = Square()
            gameObj.Square.color = color
            gameObj.Square.width = width
            debugObjects.append(gameObj)
            objects.remove(gameObj)


        def Line(self, startPoint, endPoint, color, width):
            from .Agine_main import gameDisplay
            import pygame
            startVector = self.cam.TranslateWorldVector2D(startPoint)
            endVector = self.cam.TranslateWorldVector2D(endPoint)
            pygame.draw.line(gameDisplay.display, color, [startVector.x, startVector.y],
                             [endVector.x, endVector.y], width)


        def Circle(self, position, radius, color, width):
            from .Agine_main import gameDisplay
            import pygame
            cPos = self.cam.TranslateWorldVector2D(position)
            pygame.draw.circle(gameDisplay.display, color, (cPos.x, cPos.y), radius, width)



    def TranslateWorldVector2D(self, vector2D):
        from .Agine_main import gameDisplay
        from .Objects3D import Vector3D

        newV = Vector3D()
        newV.x = (vector2D.x * gameDisplay.scale.x/2) / self.scale + gameDisplay.scale.x / 2 - self.owner.Transform.position.x
        newV.y = -(vector2D.y * gameDisplay.scale.y/2) / self.scale + gameDisplay.scale.y / 2 + self.owner.Transform.position.y
        return newV

    def ScreenToWorldVector2D(self, vector2D):
        from .Agine_main import gameDisplay
        from .Objects2D import Vector2D

        newV = Vector2D()
        newV.x = vector2D.x / ((gameDisplay.scale.x/2) / self.scale) + self.owner.Transform.position.x
        newV.y = (vector2D.y - (gameDisplay.scale.x/2 - gameDisplay.scale.y/2)) / ((gameDisplay.scale.y/2) / self.scale) + self.owner.Transform.position.y
        return newV

    def WorldToScreenVector2D(self, vector2D):
        from .Agine_main import gameDisplay
        newV = vector2D
        newV.x = newV.x + self.owner.Transform2D.position.x
        newV.y = newV.y - self.owner.Transform2D.position.y
        return newV

    def ProportionedScale(self, scale):
        from .Agine_main import gameDisplay
        return gameDisplay.scale * (scale / gameDisplay.originalScale)


class Outline(Attribute):
    def __init__(self, width = None, color = [0,0,0]):
        from Agine.Objects2D import Vector2D
        if (width == None):
            self.width = Vector2D(5, 5)
        else:
            self.width = Vector2D()
        self.color = color
