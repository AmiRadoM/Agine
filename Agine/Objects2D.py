import math
import numpy as np
import pygame
import os

assetsPath = "./assets/"



class Vector2D():
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y


    @staticmethod
    def Zero():
        return Vector2D(0,0)


    def Normalize(self):
        if (self == Vector2D.Zero()):
            return Vector2D.Zero()
        else:
            length = math.sqrt(self.x * self.x + self.y * self.y)
            return self / length


    def ToList(self):
        return [self.x, self.y]


    def __int__(self):
        return Vector2D(int(self.x), int(self.y))


    def __str__(self):
        return "Vector2D("+str(self.x)+", "+str(self.y)+")"

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __add__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x + other, self.y + other)
        if (type(other) == Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x - other, self.y - other)
        if (type(other) == Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x * other, self.y *other)
        if (type(other) == Vector2D):
            return Vector2D(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        if (type(other) == int or type(other) == float):
            return Vector2D(self.x / other, self.y / other)
        if (type(other) == Vector2D):
            return Vector2D(self.x / other.x, self.y / other.y)

    def  __neg__(self):
        return Vector2D(-self.x, -self.y)

    def __abs__(self):
        return Vector2D(abs(self.x), abs(self.y))

    def __pow__(self, power):
        result = 1
        for i in range(power):
            result = self * result
        return result




class Object2D():
    def __init__(self):
        import Agine.Attributes as Attributes
        self.name = "Object"
        self.layer = 0
        self.isVisible = True
        self.Transform2D = Attributes.Transform2D()
        object2D.append(self)

    def addAttr(self, attr):
        import Agine.Attributes as Attributes
        """
        :param attr: The name of the attribute
        """
        try:
            if(not Attributes.Attribute in eval("Attributes." + attr).__bases__):
                raise TypeError("Missing an Agine2D Attribute Name!")
            exec(f"self.{attr} = Attributes.{attr}()")
            eval(f"self.{attr}").owner = self
            eval("Attributes." + attr.lower()).append(self)
        except:
            raise TypeError("Missing an Agine2D Attribute Name!")

    # def __del__(self):
    #     object2D.remove(self)






class Sprite(Object2D):
    def __init__(self, image, color = (255,255,255,255)):
        super().__init__()

        # self.image = pygame.transform.scale(pygame.image.load(os.path.join(assetsPath,image)) ,(self.Transform2D.scale.x,self.Transform2D.scale.y))
        self.image = pygame.image.load(os.path.join(assetsPath,image))
        self.color = color
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = 3)



class ImageByPixels(Object2D):
    def __init__(self):
        super().__init__()
        self.pixels = np.zeros((self.Transform2D.scale.x, self.Transform2D.scale.y), dtype=[('r', 'i4'), ('g', 'i4'),('b', 'i4')])


class Line(Object2D):
    def __init__(self, startPoint = Vector2D(0,0), endPoint = Vector2D(0,0),color = [0,0,0], width = 1):
        super().__init__()
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color
        self.width = width




class Square(Object2D):
    def __init__(self, width = 0, color = (0,0,0), isVisible = True):
        super().__init__()
        self.width = width
        self.color = color
        self.isVisible = isVisible


class Polygon(Object2D):
    def __init__(self,points = [Vector2D(0,0),Vector2D(10,0),Vector2D(10,10)],color = (0,0,0), width = 0):
        super().__init__()
        self.points = points
        # self.translatedPoints = points
        # self.tempPoints = self.points
        self.color = color
        self.width = width



class Circle(Object2D):
    def __init__(self, radius = 100, color = (0,0,0),width = 0 ):
        super().__init__()
        self.radius = radius
        self.color = color
        self.width = width








object2D = []