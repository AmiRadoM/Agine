from Agine.Objects2D import Vector2D


class Attribute():
    pass


transform = []
class Transform2D(Attribute):
    def __init__(self):
        self.position = Vector2D.Zero()
        self.scale = Vector2D(1,1)
        self.rotation = 0


rigidbody2d = []
class Rigidbody2D(Attribute):
    def __init__(self, gravity = Vector2D(0,-9.81), mass = 1, useGravity = True):
        self.gravity = gravity  # m/s^2
        self.mass = mass  # kg
        self.velocity = Vector2D(0,0)  # m/s

        self.useGravity = useGravity  # is the rigidbody affected by gravity

        self.forces = []

    def addForce(self, force = Vector2D(0,0), type = "acceleration"):
        from Physics2D import Force2D

        self.forces.append(Force2D(force,type))


boxcollider = []
class BoxCollider(Attribute):
    def __init__(self, position = Vector2D(0,0), scale = Vector2D(0,0), isVisible = False, isTrigger = False):

        self.position = Vector2D.Zero()
        self.localPosition = Vector2D.Zero()
        self.scale = Vector2D.Zero()
        self.localScale = Vector2D(1,1)
        self.isVisible = isVisible
        self.isTrigger = isTrigger

        from .Objects2D import Square
        self.square = Square(width=2, color =(0,255,0), isVisible=False)


camera = []




class Camera(Attribute):

    def __init__(self):
        self.Draw = self.__Draw(self)
        self.scale = 5


    class __Draw():
        def __init__(self, cam):
            self.cam = cam

        def Square(self, position, scale, color, width):
            from .Agine_main import gameDisplay
            import pygame
            newPos = self.cam.ScreenToWorldVector2D(
                Vector2D(position.x - scale.x / 2,
                         position.y + scale.y / 2))
            pygame.draw.rect(gameDisplay.display, color,
                             (newPos.x, newPos.y, scale.x, scale.y),
                             width)

        def Line(self, startPoint, endPoint, color, width):
            from .Agine_main import gameDisplay
            import pygame
            startVector = self.cam.ScreenToWorldVector2D(startPoint)
            endVector = self.cam.ScreenToWorldVector2D(endPoint)
            pygame.draw.line(gameDisplay.display, color, [startVector.x, startVector.y],
                             [endVector.x, endVector.y], width)


        def Circle(self, position, radius, color, width):
            from .Agine_main import gameDisplay
            import pygame
            cPos = self.cam.ScreenToWorldVector2D(position)
            pygame.draw.circle(gameDisplay.display, color, (cPos.x, cPos.y), radius, width)



    def ScreenToWorldVector2D(self, vector2D):
        from .Agine_main import gameDisplay
        newV = vector2D
        newV.x = (newV.x * gameDisplay.scale.x/2) / self.scale + gameDisplay.scale.x / 2 - self.owner.Transform2D.position.x
        newV.y = -(newV.y * gameDisplay.scale.y/2) / self.scale + gameDisplay.scale.y / 2 + self.owner.Transform2D.position.y
        return newV

    def WorldToScreenVector2D(self, vector2D):
        from .Agine_main import gameDisplay
        newV = vector2D
        newV.x = newV.x - gameDisplay.scale.x / 2 + self.owner.Transform2D.position.x
        newV.y = newV.y - gameDisplay.scale.y / 2 + self.owner.Transform2D.position.y
        return newV

    def ProportionedScale(self, scale):
        from .Agine_main import gameDisplay
        return gameDisplay.scale * (scale / gameDisplay.originalScale)


outline = []
class Outline(Attribute):
    def __init__(self, width = Vector2D(), color = [0,0,0]):
        self.width = width
        self.color = color
