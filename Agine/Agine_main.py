import time
import math
import copy
import sys
import os
import threading
import pygame
from pygame.locals import *
import pygame.gfxdraw
from .Variables import *
import Agine.Variables as Variables
from .Objects2D import *
from .Physics2D import *
from .Collision2D import *
from .Objects3D import *
from .Input import *


cameraPos = [0,0,0]
lookDir = [0,0,1]

# crashed = {"crashed": False}



class Window():
    def __init__(self, title = "Agine Game", backgroundColor = [255, 255, 255], scale = Vector2D(1000,1000)):
        self.scale = scale
        self.originalScale = scale
        self.bgColor = backgroundColor
        self.display = pygame.display.set_mode((self.originalScale.x,self.originalScale.y),DOUBLEBUF|HWSURFACE|RESIZABLE)
        pygame.display.set_caption(title)

    def ProportionedScale(self, scale):
        return self.scale * (scale / self.originalScale)



def translatePoints(sprite):
    allX = [point.x for point in sprite.points]
    allY = [point.y for point in sprite.points]
    allX = [x * sprite.scale.x for x in allX]
    allY = [y * sprite.scale.y for y in allY]
    avarageX = sum(allX) / len(allX)
    avarageY = sum(allY) / len(allY)

    deltaX = (sprite.x - avarageX )
    deltaY = (sprite.y - avarageY)

    translatedPoints = [Vector2D((allX[i] + deltaX) + gameDisplay.display.get_width() / 2 - cameraPos[0] , -((allY[i] + deltaY) - gameDisplay.display.get_height() / 2 - cameraPos[1])) for i in range(len(allX))]

    return translatedPoints


class Draw():
    @staticmethod
    def Square(position, scale, color, width):
        x = x = position.x - scale.x / 2 + gameDisplay.display.get_width() / 2 - cameraPos[0]
        y = -(position.y + scale.y / 2 - gameDisplay.display.get_height() / 2 - cameraPos[1])
        pygame.draw.rect(gameDisplay.display, color, (x, y, scale.x, scale.y), width)

    @staticmethod
    def Line(startPoint, endPoint, color, width):
        startX = startPoint.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
        startY = -(startPoint.y - gameDisplay.display.get_height() / 2 - cameraPos[1])
        endX = endPoint.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
        endY = -(endPoint.y - gameDisplay.display.get_height() / 2 - cameraPos[1])
        pygame.draw.line(gameDisplay.display, color, [startX, startY], [endX, endY], width)

    @staticmethod
    def Circle(position, radius, color, width):
        cX = position.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
        cY = -(position.y - gameDisplay.display.get_height() / 2 - cameraPos[0])
        pygame.draw.circle(gameDisplay.display, color, (cX, cY), radius, width)

# def renderer2D():
#     # mousePos = pygame.mouse.get_pos()
#
#     # Render Background
#
#
#     # Bubble Sort Sprite Layers
#     # n = len(Sprites)
#     n = len(Sprites2D)
#     for i in range(n - 1):
#
#         for j in range(0, n - i - 1):
#
#             # if Sprites[j].layer > Sprites[j+1].layer :
#             #     Sprites[j], Sprites[j+1] = Sprites[j+1], Sprites[j]
#             if Sprites2D[j].layer > Sprites2D[j + 1].layer:
#                 Sprites2D[j], Sprites2D[j + 1] = Sprites2D[j + 1], Sprites2D[j]
#
#     # Render Sprites
#
#     # 2D!!!!
#     for sprite in Sprites2D:
#         # Sprite
#         if(sprite.isVisible):
#
#             if type(sprite) != Circle  and type(sprite) != Polygon and type(sprite) != Line:
#                 x = sprite.position.x - sprite.scale.x / 2 + gameDisplay.display.get_width() / 2 - cameraPos[0]
#                 y = -(sprite.position.y + sprite.scale.y / 2 - gameDisplay.display.get_height() / 2 - cameraPos[1])
#
#             if (type(sprite) == Line):
#                 startX = sprite.startPoint.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
#                 startY = -(sprite.startPoint.y - gameDisplay.display.get_height() / 2 - cameraPos[1])
#                 endX = sprite.endPoint.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
#                 endY = -(sprite.endPoint.y - gameDisplay.display.get_height() / 2 - cameraPos[1])
#                 pygame.draw.line(gameDisplay.display, sprite.color, [startX, startY], [endX, endY], sprite.width)
#
#             if (type(sprite) == Square):
#                 pygame.draw.rect(gameDisplay.display, sprite.color, (x, y, sprite.scale.x, sprite.scale.y), sprite.width)
#
#
#             if type(sprite) == ImageByPixels:
#                 for i in range(sprite.width):
#                     for j in range(sprite.height):
#                         pygame.gfxdraw.pixel(gameDisplay.display, int(x + i), int(y + j), sprite.pixels[j][i])
#
#             if type(sprite) == Sprite:
#                 gameDisplay.display.blit(sprite.image, (x, y))
#
#             if type(sprite) == Polygon:
#                 translatedPoints = translatePoints(sprite)
#                 sprite.translatedPoints = translatedPoints
#
#                 pygame.draw.polygon(gameDisplay.display, sprite.color, sprite.translatedPoints, sprite.width)
#
#             if type(sprite) == Circle:
#                 cX = sprite.position.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
#                 cY = -(sprite.position.y - gameDisplay.display.get_height() / 2 - cameraPos[0])
#                 pygame.draw.circle(gameDisplay.display, sprite.color, (cX, cY), sprite.radius, sprite.width)


def renderer2D():

    # Bubble Sort Sprite Layers
    # n = len(Sprites)
    n = len(object2D)
    for i in range(n - 1):

        for j in range(0, n - i - 1):

            # if Sprites[j].layer > Sprites[j+1].layer :
            #     Sprites[j], Sprites[j+1] = Sprites[j+1], Sprites[j]
            if object2D[j].layer > object2D[j + 1].layer:
                object2D[j], object2D[j + 1] = object2D[j + 1], object2D[j]

    # Render Sprites

    # 2D!!!!
    def render2D(sprite):
        if (sprite.isVisible):

            if type(sprite) != Circle and type(sprite) != Polygon and type(sprite) != Line:
                newPos = cam.Camera.ScreenToWorldVector2D(
                    Vector2D(sprite.Transform2D.position.x - sprite.Transform2D.scale.x / 2,
                             sprite.Transform2D.position.y + sprite.Transform2D.scale.y / 2))

            if (type(sprite) == Line):
                startVector = cam.Camera.ScreenToWorldVector2D(sprite.startPoint)
                endVector = cam.Camera.ScreenToWorldVector2D(sprite.endPoint)
                pygame.draw.line(gameDisplay.display, sprite.color, [startVector.x, startVector.y],
                                 [endVector.x, endVector.y], sprite.width)

            if (type(sprite) == Square):
                pygame.draw.rect(gameDisplay.display, sprite.color,
                                 (newPos.x, newPos.y, sprite.Transform2D.scale.x, sprite.Transform2D.scale.y),
                                 sprite.width)

            if type(sprite) == ImageByPixels:
                for i in range(sprite.width):
                    for j in range(sprite.height):
                        pygame.gfxdraw.pixel(gameDisplay.display, int(newPos.x + i), int(newPos.y + j),
                                             sprite.pixels[j][i])

            if type(sprite) == Sprite:
                newImage = pygame.transform.scale(sprite.image, sprite.Transform2D.scale.ToList())
                newImage = newImage.convert_alpha()

                colorImage = pygame.Surface(newImage.get_rect().size, pygame.SRCALPHA)
                colorImage.fill(sprite.color)
                newImage.blit(colorImage, (0, 0), special_flags=BLEND_RGBA_MULT)

                gameDisplay.display.blit(newImage, (newPos.x, newPos.y))

            if type(sprite) == Polygon:
                translatedPoints = translatePoints(sprite)
                sprite.translatedPoints = translatedPoints

                pygame.draw.polygon(gameDisplay.display, sprite.color, sprite.translatedPoints, sprite.width)

            if type(sprite) == Circle:
                cX = sprite.position.x + gameDisplay.display.get_width() / 2 - cameraPos[0]
                cY = -(sprite.position.y - gameDisplay.display.get_height() / 2 - cameraPos[0])
                pygame.draw.circle(gameDisplay.display, sprite.color, (cX, cY), sprite.radius, sprite.width)


    for cam in camera:
        for sprite in object2D:
            #Outline
            if (hasattr(sprite, "Outline")):
                if (type(sprite) == Sprite):
                    newPos = cam.Camera.ScreenToWorldVector2D(
                        Vector2D(sprite.Transform2D.position.x - sprite.Transform2D.scale.x / 2,
                                 sprite.Transform2D.position.y + sprite.Transform2D.scale.y / 2))

                    newImage = pygame.transform.scale(sprite.image, sprite.Transform2D.scale.ToList())

                    outline = pygame.mask.from_surface(newImage)
                    outlineSurface = outline.to_surface()
                    outlineSurface.set_colorkey([0,0,0])

                    newSurface = pygame.Surface(outlineSurface.get_size()).convert_alpha()
                    newSurface.fill([0,0,0,0])
                    newSurface.blit(outlineSurface, (0,0))

                    # colorImage = pygame.Surface(outlineSurface.get_size()).convert_alpha()
                    # colorImage.fill(sprite.Outline.color)
                    # newSurface.blit(colorImage, (0, 0), special_flags=BLEND_MULT)

                    colorImage = pygame.Surface(newSurface.get_rect().size, pygame.SRCALPHA)
                    colorImage.fill(sprite.Outline.color)
                    newSurface.blit(colorImage, (0, 0), special_flags=BLEND_RGBA_MULT)
                    newSurface.blit(outlineSurface, (0, 0), special_flags=BLEND_RGBA_MULT)

                    gameDisplay.display.blit(newSurface, (newPos.x - sprite.Outline.width.x, newPos.y))
                    gameDisplay.display.blit(newSurface, (newPos.x + sprite.Outline.width.x, newPos.y))
                    gameDisplay.display.blit(newSurface, (newPos.x, newPos.y - sprite.Outline.width.y))
                    gameDisplay.display.blit(newSurface, (newPos.x, newPos.y + sprite.Outline.width.y))
                else:
                    outline = copy.deepcopy(sprite)
                    outline.color = sprite.Outline.color

                    outline.Transform2D.position.x += sprite.Outline.width.x
                    render2D(outline)
                    outline.Transform2D.position.x -= 2 * sprite.Outline.width.x
                    render2D(outline)
                    outline.Transform2D.position.x += sprite.Outline.width.x
                    outline.Transform2D.position.y += sprite.Outline.width.y
                    render2D(outline)
                    outline.Transform2D.position.y -= 2 * sprite.Outline.width.y
                    render2D(outline)

            # Sprite
            render2D(sprite)







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






def checkClose():
    for event in pygame.event.get(pygame.QUIT):
        if event.type == pygame.QUIT:
            crashed["crashed"] = True


def checkScreenResize():
    for event in pygame.event.get(pygame.VIDEORESIZE):
        if (event.type == pygame.VIDEORESIZE):
            if (gameDisplay.scale.x != event.w and gameDisplay.scale.y == event.h):
                proportion = gameDisplay.scale.x / gameDisplay.scale.y
                gameDisplay.scale.x = event.w
                gameDisplay.scale.y = (1/proportion) * gameDisplay.scale.x
            elif (gameDisplay.scale.x == event.w and gameDisplay.scale.y != event.h):
                proportion = gameDisplay.scale.x/gameDisplay.scale.y
                gameDisplay.scale.y = event.h
                gameDisplay.scale.x = proportion * gameDisplay.scale.y
            else:
                maxDimension = max(event.w, event.h)
                if(maxDimension == event.w):
                    proportion = gameDisplay.scale.x / gameDisplay.scale.y
                    gameDisplay.scale.x = event.w
                    gameDisplay.scale.y = (1 / proportion) * gameDisplay.scale.x
                else:
                    proportion = gameDisplay.scale.x / gameDisplay.scale.y
                    gameDisplay.scale.y = event.h
                    gameDisplay.scale.x = proportion * gameDisplay.scale.y

            gameDisplay.display = pygame.display.set_mode((int(gameDisplay.scale.x), int(gameDisplay.scale.y)), DOUBLEBUF|HWSURFACE|RESIZABLE)



def Main():
    while not crashed.get("crashed"):
        Variables.deltaTime = 1/clock.get_fps()
        checkClose()
        checkScreenResize()
        for update in updateFunctions:
            update()
        gameDisplay.display.fill(gameDisplay.bgColor)
        physics2D()
        input()
        renderer2D()
        renderer3D()
        pygame.display.flip()
        clock.tick( fps)


    pygame.quit()







#Setup
pygame.init()
gameDisplay = Window()
updateFunctions = []

gameDisplay.scale = copy.copy(gameDisplay.originalScale)

while Variables.deltaTime == 0:
    for i in range(11):
        Variables.clock.tick(fps)
    Variables.deltaTime = 1/Variables.clock.get_fps()
