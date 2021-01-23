import pygame
import random
import time
import sys
import os
import threading
import Agine_main
from Agine_main import *


blue = (24,0,225)
purple = (119,60,187)
red = (153,0,0)
pink = (231,84,128)
orange = (253,106,2)
lightBlue = (137, 209, 254)
green = (91, 194, 54)
darkGreen = (0, 100, 0)
yellow = (255,211,0)

colors = {"0" : blue, "1":purple,"2":red,"3":pink,"4":orange,"5":lightBlue,"6":green}


def update():
    pass
        



def randomColor(tiles, i, j):
    color = random.randrange(0, 7)

    plusj = j+1
    minusj = j-1
    plusi = i+1
    minusi = i-1

    if(minusi<0):
        minusi = 0
    if(minusj<0):
        minusj=0
    if(plusi>6):
        plusi=6
    if (plusj>6):
        plusj = 6
        

    if(tiles[minusi][j].color == colors[str(color)]):
        color = randomColor(tiles, i, j)
    if(i==5):
        if(tiles[plusi][j].color == colors[str(color)]):
            color = randomColor(tiles, i, j)
    if (tiles[i][minusj].color == colors[str(color)]):
        color = randomColor(tiles, i, j)
    
    return color

    
class Tile():
    def __init__(self, width = 100, height = 100,x =0, y = 0, lineWidth = 7 ,color = (0,0,0), outColor = (0,0,0), layer = 0):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.color = color
        self.outColor = outColor
        self.lineWidth = lineWidth
        self.isSelected = False
        self.layer = layer
        self.inSqr = Square(name = "TileinSqr",width = self.width - self.lineWidth, height=self.height - self.lineWidth,x = self.x,y=self.y, color=self.color, layer = self.layer)
        self.outLine = Square(name = "TileinSqr",width=self.width, height=self.height, x = self.x, y = self.y, color = self.outColor, layer = self.layer-0.1)
    
    def setColor(self, color):
        self.color = color
        self.inSqr.color = color
    
    def setOutColor(self, color):
        self.outColor = color
        self.outLine.color = color


class Alex():
    def __init__(self,name, player, clickFunc = None, radius = 40, x = 0, y = 0, color = (255,255,255),outColor = (0,0,0) ,width = 10, layer = 1):
        self.name = name
        self.player = player
        self.clickFunc = clickFunc
        self.radius = radius
        self.x = x
        self.y = y
        self.color = color
        self.outColor = outColor
        self.width = width
        self.layer = layer
        self.tileI = None
        self.tileJ = None
        self.isSelected = False
        self.positionButtons = []
        self.inCir = Circle(name = "AlexInCircle-"+self.name,radius=self.radius-self.width,x =self.x, y=self.y, color = self.color , layer=self.layer)
        self.outLine = Circle(name = "AlexOutCircle-"+self.name,radius=self.radius,x =self.x, y=self.y, color = self.outColor,width = self.width, layer=self.layer)
        self.button = CircleButton(name = "AlexButton-"+self.name,radius = self.radius,x = self.x, y = self.y, isVisible = False,isActive=True,layer = self.layer+0.1, clickFunc=self.alexClick, atr = None)
    
    def Move(self, addx, addy):
        self.x += addx/1000
        self.y += addy/1000
        self.inCir.x += addx/1000
        self.inCir.y += addy/1000
        self.outLine.x += addx/1000
        self.outLine.y += addy/1000
        self.button.x += addx/1000
        self.button.y += addy/1000

    def setOutColor(self, color):
        self.outColor = color
        self.outLine.color = color

    def alexPosition(self, atr):
        x= atr[0]
        y = atr[1]
        I=atr[2]
        J=atr[3]
        self.x = x
        self.y = y
        self.tileI = I
        self.tileJ = J
        self.inCir.x = x
        self.inCir.y = y
        self.outLine.x = x
        self.outLine.y = y
        self.button.x = x
        self.button.y = y
        for btn in self.positionButtons:
            btn.remove()
            del btn
        for i in range(0, len(tiles)):
                for j in range(0, len(tiles[i])):
                    tiles[i][j].setOutColor((0,0,0))
        self.isSelected = False
        if self.player == "p1":
            self.setOutColor((255,255,255))
        elif self.player == "p2":
            self.setOutColor((0,0,0))


    def alexClick(self, atr):
        self.outLine.color = yellow
        self.isSelected = True
        rightLine = True
        straightLine = True
        leftLine = True
        
        if self.player == "p1":
            for i in range(0, len(tiles)):
                for j in range(0, len(tiles[i])):
                    tiles[i][j].setOutColor((0,0,0))
                if i>self.tileI:
                    for alex in allAlex:
                        if alex.tileI == i :
                            if alex.tileJ == self.tileJ:
                                straightLine =False
                            if alex.tileJ == self.tileJ-(i-self.tileI):
                                leftLine = False
                            if alex.tileJ == self.tileJ+(i-self.tileI):
                                rightLine = False


                    if (straightLine):
                        tiles[i][self.tileJ].setOutColor(yellow)
                        posB = SquareButton(name = "positionButton",clickFunc=self.alexPosition, atr = (tiles[i][self.tileJ].x,tiles[i][self.tileJ].y,i,self.tileJ),width = tiles[i][self.tileJ].width,height = tiles[i][self.tileJ].height,x = tiles[i][self.tileJ].x, y=tiles[i][self.tileJ].y,isVisible=False)
                        self.positionButtons.append(posB)
                    if(self.tileJ-(i-self.tileI)>=0 and leftLine):
                        tiles[i][self.tileJ-(i-self.tileI)].setOutColor(yellow)
                        posB = SquareButton(name = "positionButton",clickFunc=self.alexPosition, atr = (tiles[i][self.tileJ-(i-self.tileI)].x,tiles[i][self.tileJ-(i-self.tileI)].y,i,self.tileJ-(i-self.tileI)),width = tiles[i][self.tileJ-(i-self.tileI)].width,height = tiles[i][self.tileJ-(i-self.tileI)].height,x = tiles[i][self.tileJ-(i-self.tileI)].x, y=tiles[i][self.tileJ-(i-self.tileI)].y,isVisible=False)
                        self.positionButtons.append(posB)
                    if(self.tileJ+(i-self.tileI)<=6 and rightLine):
                        tiles[i][self.tileJ+(i-self.tileI)].setOutColor(yellow)
                        posB = SquareButton(name = "positionButton",clickFunc=self.alexPosition, atr = (tiles[i][self.tileJ+(i-self.tileI)].x,tiles[i][self.tileJ+(i-self.tileI)].y,i, self.tileJ+i),width = tiles[i][self.tileJ+(i-self.tileI)].width,height = tiles[i][self.tileJ+(i-self.tileI)].height,x = tiles[i][self.tileJ+(i-self.tileI)].x, y=tiles[i][self.tileJ+(i-self.tileI)].y,isVisible=False)
                        self.positionButtons.append(posB)
                    


            
        elif self.player == "p2":
            for i in range(len(tiles)-1,-1,-1):
                for j in range(0, len(tiles[i])):
                    tiles[i][j].setOutColor((0,0,0))
                if i<=self.tileI:
                    tiles[i][self.tileJ].setOutColor(yellow)
        for alex in allAlex:
            if self.name != alex.name:
                if alex.player == "p1":
                    alex.outLine.color = (255,255,255)
                if alex.player == "p2":
                    alex.outLine.color = (0,0,0)
                alex.isSelected = False




    

if __name__ == "__main__":

    Sprite(name = "BG",image = "greenBG.jpg", width = Agine_main.gameDisplay.width, height = Agine_main.gameDisplay.height,x=0, y=0, layer = -500, color = (255,255,255))

    #Set Up Board
    boardX = -475
    boardY = 300


    tiles = [[],[],[],[],[],[],[]]
    player1alex = []
    player2alex = []
    allAlex = []

    for i in range(0,7):
        tile1 = Tile(x = boardX + i*100, y = boardY, color=colors[str(i)])
        alex1 = Alex(name = "alex" + str(i),player="p1", x = boardX + i*100,y=boardY,color =colors[str(i)], outColor = (255,255,255))
        tile2 = Tile(x = boardX + i*100, y = - boardY, color=colors[str(-(i+2)+8)])
        alex2 = Alex(name = "alex" + str(i),player="p2", x = boardX + i*100,y=-boardY,color =colors[str(-(i+2)+8)], outColor = (0,0,0))
        alex1.tileI = 0
        alex1.tileJ = i
        alex2.tileI = 6
        alex2.tileJ = i
        tiles[0].append(tile1)
        player1alex.append(alex1)
        allAlex.append(alex1)
        tiles[6].append(tile2)
        player2alex.append(alex2)
        allAlex.append(alex2)

    for i in range(1,6):
        for j in range(0,7):

            tile = Tile(x = boardX + j*100, y = boardY - i*100)
            tiles[i].append(tile)
            color = randomColor(tiles,i, j)
            tile.setColor(colors[str(color)])
    
    #Threading
    updateThread = threading.Thread(target=update, args=())
    updateThread.start()


if __name__ == "__main__":
    Agine_main.checkClose(Agine_main.crashed)