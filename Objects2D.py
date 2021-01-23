from Physics2D import *
from Attributes import  *
import numpy as np
import os

assetsPath = "./assets/"



class Vector2D():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if(type(other) == int or type(other) == float):
            self.x += other
            self.y += other
        if(type(other) == Vector2D):
            self.x += other.x
            self.y += other.y

    def __sub__(self, other):
        if(type(other) == int or type(other) == float):
            self.x -= other
            self.y -= other
        if(type(other) == Vector2D):
            self.x -= other.x
            self.y -= other.y


class object2D():
    def addAttr(self, attr):
        """
        :param attr: The name of the attribute
        """
        if attr == "Rigidbody2D":
            self.Rigidbody2D = Rigidbody2D()
            RB2D.append(self)
        elif(attr == "BoxCollider"):
            self.BoxCollider = BoxCollider()
            BC.append(self)
        else:
            raise ValueError("Missing an Agine2D Attribute Name!")



class Sprite(object2D):
    def __init__(self, image, name = "", width = 100, height = 100, color = (255,255,255,255), x =0, y = 0, layer = 0):
        self.width = width
        self.height = height
        self.name = name
        if (width != None or height != None):
            self.image = pygame.transform.scale(pygame.image.load(os.path.join(assetsPath,image)) ,(self.width,self.height))
        else:
            self.image = pygame.image.load(os.path.join(assetsPath, image))
            

        #Ignore the ERROR, It Works
        #            |
        #            v
        colorImage = pygame.Surface(self.image.get_size()).convert_alpha()
        colorImage.fill(color)
        self.image.blit(colorImage, (0,0), special_flags = 3)

        self.x = x
        self.y = y
        self.layer = layer
        Sprites2D.append(self)
    
    def move(self, x, y):
        self.x += x/1000
        self.y += y/1000

    def __del__(self):
        Sprites2D.remove(self)

class ImageByPixels(object2D):
    def __init__(self, name = "", position = [0,0], scale = [50,50], layer = 0):
        self.name = name
        self.x = position[0]
        self.y = position[1]
        self.width = scale [0]
        self.height = scale [1]
        self.pixels = np.zeros((scale[1], scale[0]), dtype=[('r', 'i4'), ('g', 'i4'),('b', 'i4')])
        self.layer = 0
        Sprites2D.append(self)

    def __del__(self):
        Sprites2D.remove(self)

class Line(object2D):
    def __init__(self,name = "", startPoint = [0,0], endPoint = [0,0],color = [0,0,0], width = 1, isVisible = True, layer = 0):
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
    def __init__(self, name = "", x =0, y = 0, scale = [200,200], width = 0, color = (0,0,0), isVisible = True, layer = 0):
        self.name = name
        self.scale = scale
        self.x = x
        self.y = y
        # self.points = [[(x - scale[0]/2) / scale[0],(y - scale[1]/2) / scale[1]],[(x + scale[0]/2) / scale[0],(y - scale[1]/2) / scale[1]],[(x + scale[0]/2) / scale[0],(y + scale[1]/2) / scale[1]],[(x - scale[0]/2) / scale[0],(y + scale[1]/2) / scale[1]]]
        self.width = width
        self.color = color
        self.isVisible = isVisible
        self.layer = layer
        Sprites2D.append(self)

    def move(self, addx, addy):
        self.x += addx/1000
        self.y += addy/1000

    def __del__(self):
        Sprites2D.remove(self)

class Polygon(object2D):
    def __init__(self, name = "",x =0,y=0,scale = [10,10],points = [[0,0],[10,0],[10,10]],color = (0,0,0), width = 0, isVisible = True, layer = 0):
        self.name = name
        self.x = x
        self.y = y
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

    def move(self, addx, addy):
        self.x += addx
        self.y += addy

class Circle(object2D):
    def __init__(self, name = "", radius = 100, x = 0, y = 0, color = (0,0,0),width = 0 , isVisible = True, layer = 0):
        self.name = name
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.isVisible = isVisible
        self.layer = layer
        Sprites2D.append(self)

    def move(self, addx, addy):
        self.x += addx
        self.y += addy

    def __del__(self):
        Sprites2D.remove(self)


class CircleButton(object2D):
    def __init__(self,  clickFunc, atr,name = "", radius = 100, x = 0, y = 0, color = (0,0,0),width = 0, layer = 0, isVisible = True, isActive = True):
        self.name = name
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.layer = layer
        self.isActive = isActive
        self.isVisible = isVisible
        self.clickFunc = clickFunc
        self.atr = atr
        self.clicked = False
        Sprites2D.append(self)

    def move(self, addx, addy):
        self.x += addx/1000
        self.y += addy/1000

    def __del__(self):
        Sprites2D.remove(self)

class SquareButton(object2D):
    def __init__(self, clickFunc, atr, name = "", width = 200, height = 200, x = 0, y = 0, color = (0,0,0), layer = 0, isVisible = True, isActive = True):
        self.name = name
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.height = height
        self.layer = layer
        self.isActive = isActive
        self.isVisible = isVisible
        self.clickFunc = clickFunc
        self.atr = atr
        self.clicked = False
        Sprites2D.append(self)

    def move(self, addx, addy):
        self.x += addx/1000
        self.y += addy/1000

    def __del__(self):
        Sprites2D.remove(self)



Sprites2D = []