
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

    def __str__(self):
        return "Vector2D("+str(self.x)+", "+str(self.y)+")"

    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

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



class object2D():
    def addAttr(self, attr):
        import Attributes
        """
        :param attr: The name of the attribute
        """
        # if attr == "Rigidbody2D":
        #     self.Rigidbody2D = Attributes.Rigidbody2D()
        #     Attributes.RB2D.append(self)
        # elif(attr == "BoxCollider"):
        #     self.BoxCollider = Attributes.BoxCollider()
        #     Attributes.BC.append(self)
        # else:
        #     raise ValueError("Missing an Agine2D Attribute Name!")

        # setattr(self, "attr", eval(""+attr + "()"))
        try:
            exec(f"self.{attr} = Attributes.{attr}()")
            eval("Attributes." + attr.lower()).append(self)
        except:
            raise ValueError("Missing an Agine2D Attribute Name!")





class Sprite(object2D):
    def __init__(self, image, name = "", scale = Vector2D(100,100), color = (255,255,255,255), position = Vector2D(0,0), layer = 0):
        self.scale = scale
        self.name = name
        if (scale.x != None or scale.y != None):
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(assetsPath,image)) ,(self.scale.x,self.scale.y))
        else:
            self.image = pygame.image.load(os.path.join(assetsPath, image))
            

        #Ignore the ERROR, It Works
        #            |
        #            v
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = 3)

        self.position = position
        self.layer = layer
        Sprites2D.append(self)


    def __del__(self):
        Sprites2D.remove(self)

class ImageByPixels(object2D):
    def __init__(self, name = "", position = Vector2D(0,0), scale = Vector2D(50,50), layer = 0):
        self.name = name
        self.position = position
        self.scale = scale
        self.pixels = np.zeros((scale.y, scale.x), dtype=[('r', 'i4'), ('g', 'i4'),('b', 'i4')])
        self.layer = 0
        Sprites2D.append(self)

    def __del__(self):
        Sprites2D.remove(self)

class Line(object2D):
    def __init__(self,name = "", startPoint = Vector2D(0,0), endPoint = Vector2D(0,0),color = [0,0,0], width = 1, isVisible = True, layer = 0):
        self.name = name
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.color = color
        self.width = width
        self.isVisible = isVisible
        self.layer = layer
        Sprites2D.append(self)

    def __del__(self):
        Sprites2D.remove(self)


class Square(object2D):
    def __init__(self, name = "", position = Vector2D(0,0), scale =Vector2D(100,100), width = 0, color = (0,0,0), isVisible = True, layer = 0):
        self.name = name
        self.scale = scale
        self.position = position
        # self.points = [[(x - scale[0]/2) / scale[0],(y - scale[1]/2) / scale[1]],[(x + scale[0]/2) / scale[0],(y - scale[1]/2) / scale[1]],[(x + scale[0]/2) / scale[0],(y + scale[1]/2) / scale[1]],[(x - scale[0]/2) / scale[0],(y + scale[1]/2) / scale[1]]]
        self.width = width
        self.color = color
        self.isVisible = isVisible
        self.layer = layer
        Sprites2D.append(self)


    def __del__(self):
        Sprites2D.remove(self)

class Polygon(object2D):
    def __init__(self, name = "",position = Vector2D(0,0),scale = Vector2D(10,10),points = [Vector2D(0,0),Vector2D(10,0),Vector2D(10,10)],color = (0,0,0), width = 0, isVisible = True, layer = 0):
        self.name = name
        self.position = position
        self.scale = scale
        self.points = points
        self.translatedPoints = points
        self.tempPoints = self.points
        self.color = color
        self.width = width
        self.isVisible = isVisible
        self.layer = layer
        Sprites2D.append(self)

    def __del__(self):
        Sprites2D.remove(self)


class Circle(object2D):
    def __init__(self, name = "", radius = 100, position = Vector2D(0,0), color = (0,0,0),width = 0 , isVisible = True, layer = 0):
        self.name = name
        self.radius = radius
        self.position = position
        self.color = color
        self.width = width
        self.isVisible = isVisible
        self.layer = layer
        Sprites2D.append(self)


    def __del__(self):
        Sprites2D.remove(self)





Sprites2D = []