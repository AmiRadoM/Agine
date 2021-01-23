import time
import math
import copy
import sys
import os
import threading
import pygame
from pygame.locals import *
import pygame.gfxdraw
from Variables import *
import Variables
from Objects2D import *
from Physics2D import *
from Collision2D import *
from Objects3D import *
from Input import *


cameraPos = [0,0,0]
lookDir = [0,0,1]
InputKeyboard = {"a": False, "b": False, "c": False, "d": False, "e": False, "f": False, "g": False, "h": False, "i": False, "j": False, "k": False, "l": False, "m": False, "n": False, "o": False, "p": False, "q": False, "r": False, "s": False, "t": False, "u": False, "v": False, "w": False, "x": False, "y": False, "z": False, "space": False, "lshift": False,"up": False, "down": False,"left": False,"right": False, }
InputMouse = {"click0" : False, "click1" : False, "click2": False, "click0Down":False}
# crashed = {"crashed": False}



class Window():
    def __init__(self, title = "Agine Game", backgroundColor = [255, 255, 255], width = 1000, height = 1000):
        self.display = pygame.display.set_mode((width,height),DOUBLEBUF|HWSURFACE|RESIZABLE)
        #self.display = pygame.display.set_mode((width,height),DOUBLEBUF|OPENGL)
        self.bgColor = backgroundColor
        self.width = width
        self.height = height

        pygame.display.set_caption(title)


def translatePoints(sprite):
    allX = [point[0] for point in sprite.points]
    allY = [point[1] for point in sprite.points]
    allX = [x * sprite.scale[0] for x in allX]
    allY = [y * sprite.scale[1] for y in allY]
    avarageX = sum(allX) / len(allX)
    avarageY = sum(allY) / len(allY)

    deltaX = (sprite.x - avarageX )
    deltaY = (sprite.y - avarageY)

    translatedPoints = [[(allX[i] + deltaX) + gameDisplay.display.get_width() / 2 - cameraPos[0] , -((allY[i] + deltaY) - gameDisplay.display.get_height() / 2 - cameraPos[1])] for i in range(len(allX))]

    # translatedPoints = [[a[i], b[i]] for i in range(len(a))]
    #
    # for i in range(len(translatedPoints)):
    #     translatedPoints[i][0] = (sprite.points[i][0] * sprite.scale[0] + sprite.x - (
    #                 a[-1] - a[:1][0]) / 2 + gameDisplay.display.get_width() / 2 - cameraPos[0])
    #
    # for j in range((int)(len(translatedPoints))):
    #     translatedPoints[j][1] = -(sprite.points[j][1] * sprite.scale[1] + sprite.y + (
    #                 b[-1] - b[:1][0]) / 2 - gameDisplay.display.get_height() / 2 - cameraPos[1])
    #
    return translatedPoints

        
def renderer2D():
    # mousePos = pygame.mouse.get_pos()

    # Render Background
    gameDisplay.display.fill(gameDisplay.bgColor)


    # Bubble Sort Sprite Layers
    # n = len(Sprites)
    n = len(Sprites2D)
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            # if Sprites[j].layer > Sprites[j+1].layer :
            #     Sprites[j], Sprites[j+1] = Sprites[j+1], Sprites[j]
            if Sprites2D[j].layer > Sprites2D[j + 1].layer:
                Sprites2D[j], Sprites2D[j + 1] = Sprites2D[j + 1], Sprites2D[j]

    # Render Sprites

    # 2D!!!!
    for sprite in Sprites2D:
        # Sprite
        if(sprite.isVisible):

            if type(sprite) != Circle and type(sprite) != CircleButton and type(sprite) != Polygon and type(sprite) != Line:
                x = sprite.x - sprite.scale[0] / 2 + gameDisplay.display.get_width() / 2 - cameraPos[0]
                y = -(sprite.y + sprite.scale[1] / 2 - gameDisplay.display.get_height() / 2 - cameraPos[1])

            if (type(sprite) == Line):
                startX = sprite.startPoint[0] + gameDisplay.display.get_width() / 2 - cameraPos[0]
                startY = -(sprite.startPoint[1] - gameDisplay.display.get_height() / 2 - cameraPos[1])
                endX = sprite.endPoint[0] + gameDisplay.display.get_width() / 2 - cameraPos[0]
                endY = -(sprite.endPoint[1] - gameDisplay.display.get_height() / 2 - cameraPos[1])
                pygame.draw.line(gameDisplay.display, sprite.color, [startX, startY], [endX, endY], sprite.width)

            if (type(sprite) == Square):
                pygame.draw.rect(gameDisplay.display, sprite.color, (x, y, sprite.scale[0], sprite.scale[1]), sprite.width)

            if type(sprite) == SquareButton:
                if (sprite.isVisible):
                    pygame.draw.rect(gameDisplay.display, sprite.color, (x, y, sprite.width, sprite.height))
                if (sprite.isActive):
                    if not InputMouse["click0"]:
                        sprite.clicked = False

                    if x + sprite.width > mousePos[0] > x and y + sprite.height > mousePos[1] > y:

                        if InputMouse["click0"]:

                            if not sprite.clicked and not InputMouse["click0Down"]:
                                sprite.clickFunc(sprite.atr)
                                sprite.clicked = True

                            pass
                            InputMouse["click0Down"] = True

            if type(sprite) == ImageByPixels:
                for i in range(sprite.width):
                    for j in range(sprite.height):
                        pygame.gfxdraw.pixel(gameDisplay.display, int(x + i), int(y + j), sprite.pixels[j][i])

            if type(sprite) == Sprite:
                gameDisplay.display.blit(sprite.image, (x, y))

            if type(sprite) == Polygon:
                translatedPoints = translatePoints(sprite)
                sprite.translatedPoints = translatedPoints

                pygame.draw.polygon(gameDisplay.display, sprite.color, sprite.translatedPoints, sprite.width)

            if type(sprite) == Circle:
                cX = sprite.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
                cY = -(sprite.y - gameDisplay.display.get_height() / 2 - cameraPos[0])
                pygame.draw.circle(gameDisplay.display, sprite.color, (int(cX), int(cY)), sprite.radius, sprite.width)

            if type(sprite) == CircleButton:

                cX = sprite.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
                cY = -(sprite.y - gameDisplay.display.get_height() / 2 - cameraPos[1])
                if (sprite.isVisible):
                    pygame.draw.circle(gameDisplay.display, sprite.color, (int(cX), int(cY)), sprite.radius, sprite.width)
                if sprite.isActive:

                    if not InputMouse["click0"]:
                        sprite.clicked = False

                    if cX + sprite.radius > mousePos[0] > cX - sprite.radius and cY + sprite.radius > mousePos[
                        1] > cY - sprite.radius:

                        if InputMouse["click0"] and not InputMouse["click0Down"]:
                            if not sprite.clicked:
                                sprite.clickFunc(sprite.atr)
                                sprite.clicked = True

                            pass
                            InputMouse["click0Down"] = True

    pygame.display.flip()




def renderer3D():
    # n = len(Sprites3D)
    # for i in range(n-1):
    #     for j in range(0, n-i-1):
    #
    #         if Sprites3D[j].layer > Sprites3D[j+1].layer :
    #             Sprites3D[j], Sprites3D[j+1] = Sprites3D[j+1], Sprites3D[j]
    trianglesToRaster = []

    for sprite in Sprites3D:

        # Projection Matrix
        mProj = MatrixMakeProjection(90, gameDisplay.height / gameDisplay.width, 0, 1000)
        # Rotation Matrices
        mZ = MatrixMakeRotationZ(sprite.rotationz)
        mX = MatrixMakeRotationX(math.radians(sprite.rotationx + 180))
        mY = MatrixMakeRotationY(sprite.rotationy)
        # Translation Matrix
        mTrans = MatrixMakeTranslation(0, 0, 0)
        # World Matrix
        mWorld = MatrixMakeIdentity()
        mWorld = MatrixMultiplyMatrix(mZ, mX)
        mWorld = MatrixMultiplyMatrix(mWorld, mTrans)
        # Camera Matrix
        Up = [0, 1, 0]
        Target = Vector3DAdd(cameraPos, lookDir)
        mCamera = MatrixPointAt(cameraPos, Target, Up)
        mView = MatrixQuickInverseForLookAt(mCamera)

        for triangle in sprite.mesh.Triangles:
            triProjected = Triangle3D()
            triTranslated = copy.deepcopy(triangle)

            # Rotation
            # Z

            triTranslated.p[0][0] = triangle.p[0][0] * mZ.m[0][0] + triangle.p[0][1] * mZ.m[1][0]
            triTranslated.p[1][0] = triangle.p[1][0] * mZ.m[0][0] + triangle.p[1][1] * mZ.m[1][0]
            triTranslated.p[2][0] = triangle.p[2][0] * mZ.m[0][0] + triangle.p[2][1] * mZ.m[1][0]
            triTranslated.p[0][1] = triangle.p[0][1] * mZ.m[1][1] + triangle.p[0][0] * mZ.m[0][1]
            triTranslated.p[1][1] = triangle.p[1][1] * mZ.m[1][1] + triangle.p[1][0] * mZ.m[0][1]
            triTranslated.p[2][1] = triangle.p[2][1] * mZ.m[1][1] + triangle.p[2][0] * mZ.m[0][1]

            # X
            tempTriangle = copy.deepcopy(triTranslated)

            triTranslated.p[0][1] = tempTriangle.p[0][1] * mX.m[1][1] + tempTriangle.p[0][2] * mX.m[2][1]
            triTranslated.p[1][1] = tempTriangle.p[1][1] * mX.m[1][1] + tempTriangle.p[1][2] * mX.m[2][1]
            triTranslated.p[2][1] = tempTriangle.p[2][1] * mX.m[1][1] + tempTriangle.p[2][2] * mX.m[2][1]
            triTranslated.p[0][2] = tempTriangle.p[0][2] * mX.m[2][2] + tempTriangle.p[0][1] * mX.m[1][2]
            triTranslated.p[1][2] = tempTriangle.p[1][2] * mX.m[2][2] + tempTriangle.p[1][1] * mX.m[1][2]
            triTranslated.p[2][2] = tempTriangle.p[2][2] * mX.m[2][2] + tempTriangle.p[2][1] * mX.m[1][2]

            # Y
            tempTriangle = copy.deepcopy(triTranslated)

            triTranslated.p[0][0] = tempTriangle.p[0][0] * mY.m[0][0] + tempTriangle.p[0][2] * mY.m[0][2]
            triTranslated.p[1][0] = tempTriangle.p[1][0] * mY.m[0][0] + tempTriangle.p[1][2] * mY.m[0][2]
            triTranslated.p[2][0] = tempTriangle.p[2][0] * mY.m[0][0] + tempTriangle.p[2][2] * mY.m[0][2]
            triTranslated.p[0][2] = tempTriangle.p[0][2] * mY.m[2][2] + tempTriangle.p[0][0] * mY.m[2][0]
            triTranslated.p[1][2] = tempTriangle.p[1][2] * mY.m[2][2] + tempTriangle.p[1][0] * mY.m[2][0]
            triTranslated.p[2][2] = tempTriangle.p[2][2] * mY.m[2][2] + tempTriangle.p[2][0] * mY.m[2][0]

            # Scale
            triTranslated.p[0][0] *= sprite.scalex
            triTranslated.p[1][0] *= sprite.scalex
            triTranslated.p[2][0] *= sprite.scalex
            triTranslated.p[0][1] *= sprite.scaley
            triTranslated.p[1][1] *= sprite.scaley
            triTranslated.p[2][1] *= sprite.scaley
            triTranslated.p[0][2] *= sprite.scalez
            triTranslated.p[1][2] *= sprite.scalez
            triTranslated.p[2][2] *= sprite.scalez

            # Position
            triTranslated.p[0][0] += sprite.x
            triTranslated.p[1][0] += sprite.x
            triTranslated.p[2][0] += sprite.x
            triTranslated.p[0][1] += sprite.y
            triTranslated.p[1][1] += sprite.y
            triTranslated.p[2][1] += sprite.y
            triTranslated.p[0][2] += sprite.z
            triTranslated.p[1][2] += sprite.z
            triTranslated.p[2][2] += sprite.z

            # Getting Normal of Triangle
            normal = [0, 0, 0]
            line1 = [0, 0, 0]
            line2 = [0, 0, 0]
            line1 = Vector3DSub(triTranslated.p[1], triTranslated.p[0])
            line2 = Vector3DSub(triTranslated.p[2], triTranslated.p[0])
            normal = Vector3DCrossProduct(line1, line2)
            normal = Vector3DNormalise(normal)

            # If checks if player sees the triangle so the engine shold render it
            cameraRay = Vector3DSub(triTranslated.p[0], cameraPos)
            if (Vector3DDotProduct(normal, cameraRay) < 0):
                # if(True):

                # Illumination
                lightDir = [0, -1, -1]
                lightDir = Vector3DNormalise(lightDir)

                dp = max(0.1, Vector3DDotProduct(lightDir, normal))
                triProjected.color = Vector3DMultVector3D(triProjected.color, Vector3DDiv(GetColorShading(dp), 255))

                # Convert World Space ---> View Space
                tempTriangle = copy.deepcopy(triTranslated)
                triTranslated.p[0] = MultiplyMatrixVector(tempTriangle.p[0], triTranslated.p[0], mView)
                triTranslated.p[1] = MultiplyMatrixVector(tempTriangle.p[1], triTranslated.p[1], mView)
                triTranslated.p[2] = MultiplyMatrixVector(tempTriangle.p[2], triTranslated.p[2], mView)

                # Clip Viewed Triangle agains near
                clipped = TriangleClipAgainstPlane([0, 0, 0.1], [0, 0, 1.0], triTranslated)

                for n in range(len(clipped)):
                    # Project Triangles from 3D ---> 2D

                    triProjected.p[0] = MultiplyMatrixVector(clipped[n].p[0], triProjected.p[0], mProj)
                    triProjected.p[1] = MultiplyMatrixVector(clipped[n].p[1], triProjected.p[1], mProj)
                    triProjected.p[2] = MultiplyMatrixVector(clipped[n].p[2], triProjected.p[2], mProj)

                    # Scale to View
                    triProjected.p[0][0] += 1.0
                    triProjected.p[0][1] += 1.0
                    triProjected.p[1][0] += 1.0
                    triProjected.p[1][1] += 1.0
                    triProjected.p[2][0] += 1.0
                    triProjected.p[2][1] += 1.0

                    triProjected.p[0][0] *= 0.5 * gameDisplay.width
                    triProjected.p[0][1] *= 0.5 * gameDisplay.height
                    triProjected.p[1][0] *= 0.5 * gameDisplay.width
                    triProjected.p[1][1] *= 0.5 * gameDisplay.height
                    triProjected.p[2][0] *= 0.5 * gameDisplay.width
                    triProjected.p[2][1] *= 0.5 * gameDisplay.height

                    trianglesToRaster.append(copy.deepcopy(triProjected))

    trianglesToRaster.sort(key=lambda tri: (tri.p[0][2] + tri.p[1][2] + tri.p[2][2]) / 3.0, reverse=True)

    # Clipping on boarders of the screen
    for tri in trianglesToRaster:
        # # Draws the Triangles
        # pygame.draw.polygon(gameDisplay.display,tri.color, [[tri.p[0][0],tri.p[0][1]],[tri.p[1][0],tri.p[1][1]],[tri.p[2][0],tri.p[2][1]]])
        # #pygame.gfxdraw.polygon(gameDisplay.display, [[tri.p[0][0],tri.p[0][1]],[tri.p[1][0],tri.p[1][1]],[tri.p[2][0],tri.p[2][1]]],tri.color)
        #
        # #Draws the border of the Triangles
        # pygame.draw.polygon(gameDisplay.display, (0,0,0), [[tri.p[0][0], tri.p[0][1]],[tri.p[1][0], tri.p[1][1]],[tri.p[2][0], tri.p[2][1]]],7)
        # #pygame.gfxdraw.aapolygon(gameDisplay.display, [[tri.p[0][0], tri.p[0][1]],[tri.p[1][0], tri.p[1][1]],[tri.p[2][0], tri.p[2][1]]], (0,0,0))

        listTriangles = []
        listTriangles.append(tri)
        newTriangles = 1

        for p in range(4):
            while (newTriangles > 0):
                test = listTriangles[-1]
                listTriangles.pop()
                newTriangles -= 1

                if (p == 0):
                    clipped = TriangleClipAgainstPlane([0, 0, 0], [0, 1, 0], test)
                elif (p == 1):
                    clipped = TriangleClipAgainstPlane([0, gameDisplay.display.get_height() - 1, 0], [0, -1, 0], test)
                elif (p == 2):
                    clipped = TriangleClipAgainstPlane([0, 0, 0], [1, 0, 0], test)
                elif (p == 3):
                    clipped = TriangleClipAgainstPlane([gameDisplay.display.get_width() - 1, 0, 0], [-1, 0, 0], test)

                for w in range(len(clipped)):
                    listTriangles.append(clipped[w])

            newTriangles = len(listTriangles)

        for newTri in listTriangles:
            # Draws the Triangles
            pygame.draw.polygon(gameDisplay.display, newTri.color,
                                [[newTri.p[0][0], newTri.p[0][1]], [newTri.p[1][0], newTri.p[1][1]],
                                 [newTri.p[2][0], newTri.p[2][1]]])
            # pygame.gfxdraw.polygon(gameDisplay.display, [[newTri.p[0][0],newTri.p[0][1]],[newTri.p[1][0],newTri.p[1][1]],[newTri.p[2][0],newTri.p[2][1]]],newTri.color)

            # Draws the border of the Triangles
            # pygame.draw.polygon(gameDisplay.display, (0,0,0), [[newTri.p[0][0], newTri.p[0][1]],[newTri.p[1][0], newTri.p[1][1]],[newTri.p[2][0], newTri.p[2][1]]],7)
            # pygame.gfxdraw.aapolygon(gameDisplay.display, [[newTri.p[0][0], newTri.p[0][1]],[newTri.p[1][0], newTri.p[1][1]],[newTri.p[2][0], newTri.p[2][1]]], (0,0,0))

    pygame.display.flip()


def __gameInput():
    # global crashed
    while not crashed.get("crashed"):
        
        pressed = pygame.key.get_pressed()
        clicked = pygame.mouse.get_pressed()

        #keyboard
        if pressed[pygame.K_w]:
            InputKeyboard["w"] = True


        else:
            InputKeyboard["w"] = False
            
        if pressed[pygame.K_s]:
            InputKeyboard["s"] = True





        else:
            InputKeyboard["s"] = False

        if pressed[pygame.K_a]:
            InputKeyboard["a"] = True




        else:
            InputKeyboard["a"] = False

        if pressed[pygame.K_d]:
            InputKeyboard["d"] = True


        else:
            InputKeyboard["d"] = False

        if pressed[pygame.K_SPACE]:
            InputKeyboard["space"] = True


        else:
            InputKeyboard["space"] = False

        if pressed[pygame.K_LSHIFT]:
            InputKeyboard["lshift"] = True


        else:
            InputKeyboard["lshift"] = False

        if pressed[pygame.K_UP]:
            InputKeyboard["up"] = True


        else:
            InputKeyboard["up"] = False

        if pressed[pygame.K_DOWN]:
            InputKeyboard["down"] = True


        else:
            InputKeyboard["down"] = False

        if pressed[pygame.K_LEFT]:
            InputKeyboard["left"] = True


        else:
            InputKeyboard["left"] = False

        if pressed[pygame.K_RIGHT]:
            InputKeyboard["right"] = True


        else:
            InputKeyboard["right"] = False

        
        #mouse
        if clicked[0] == 1:
            InputMouse["click0"] = True
            
        else:
            InputMouse["click0"] = False
            InputMouse["click0Down"] = False



def checkClose():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed["crashed"] = True





def Main():
    while not crashed.get("crashed"):
        Variables.deltaTime = 1/clock.get_fps()
        checkClose()
        physics2D()
        input()
        collision2D()
        renderer2D()
        # renderer3D()
        clock.tick(fps)


    pygame.quit()







#Setup
pygame.init()
gameDisplay = Window()

while Variables.deltaTime == 0:
    for i in range(11):
        clock.tick(fps)
    Variables.deltaTime = 1/clock.get_fps()
