from Agine import *
import random


class Block(GameObject):
    def __init__(self, position=Vector2D.Zero()):
        super().__init__()
        self.position = position
        self.trigger = False

def Trigger(blk):
    blk.trigger = True

class Tetramino(list):
    def __init__(self):
        super().__init__()
        self.blocks = []
        self.size = 0
        self.position = Vector2D(0,0)


def GameOver():
    pass

def CreateBlock():
    block = Block()
    block.Square = Square()
    block.BoxCollider = BoxCollider()
    block.BoxCollider.isTrigger = True
    block.BoxCollider.onTrigger.append(lambda a: Trigger(a))
    block.Transform.scale = Vector3D(0.45, 0.45, 1)
    return block

def CreateTetramino(tetraminoId):
    tetramino = Tetramino()
    if (tetraminoId == 0):
        #I
        tetramino.size = 4

        newBlock = CreateBlock()
        newBlock.Square.color = [137,207,240]
        newBlock.Transform.position = Vector3D(0, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [137, 207, 240]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [137, 207, 240]
        newBlock.Transform.position = Vector3D(1, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [137, 207, 240]
        newBlock.Transform.position = Vector3D(1.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)
    elif (tetraminoId == 1):
        #S
        tetramino.size = 3

        newBlock = CreateBlock()
        newBlock.Square.color = [124, 252, 0]
        newBlock.Transform.position = Vector3D(0, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [124, 252, 0]
        newBlock.Transform.position = Vector3D(0.5, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [124, 252, 0]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [124, 252, 0]
        newBlock.Transform.position = Vector3D(1, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)
    elif (tetraminoId == 2):
        #Z
        tetramino.size = 3

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 0, 0]
        newBlock.Transform.position = Vector3D(0, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 0, 0]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 0, 0]
        newBlock.Transform.position = Vector3D(0.5, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 0, 0]
        newBlock.Transform.position = Vector3D(1, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)
    elif (tetraminoId == 3):
        #L
        tetramino.size = 3

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 140, 0]
        newBlock.Transform.position = Vector3D(0, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 140, 0]
        newBlock.Transform.position = Vector3D(0, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 140, 0]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255, 140, 0]
        newBlock.Transform.position = Vector3D(1, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)
    elif (tetraminoId == 4):
        #J
        tetramino.size = 3

        newBlock = CreateBlock()
        newBlock.Square.color = [0,0,205]
        newBlock.Transform.position = Vector3D(0, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [0,0,205]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [0,0,205]
        newBlock.Transform.position = Vector3D(1, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [0,0,205]
        newBlock.Transform.position = Vector3D(1, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)
    elif (tetraminoId == 5):
        #T
        tetramino.size = 3

        newBlock = CreateBlock()
        newBlock.Square.color = [138,43,226]
        newBlock.Transform.position = Vector3D(0,  -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [138,43,226]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [138,43,226]
        newBlock.Transform.position = Vector3D(0.5, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [138,43,226]
        newBlock.Transform.position = Vector3D(1, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)
    elif (tetraminoId == 6):
        #O
        tetramino.size = 4

        newBlock = CreateBlock()
        newBlock.Square.color = [255,215,0]
        newBlock.Transform.position = Vector3D(0.5, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255,215,0]
        newBlock.Transform.position = Vector3D(0.5, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255,215,0]
        newBlock.Transform.position = Vector3D(1, -0.5, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

        newBlock = CreateBlock()
        newBlock.Square.color = [255,215,0]
        newBlock.Transform.position = Vector3D(1, -1, 0)
        newBlock.position = Vector2D(newBlock.Transform.position.x*2, -newBlock.Transform.position.y*2)
        tetramino.blocks.append(newBlock)

    return tetramino

def MoveTetramino(tetramino, x, y):
    tetramino.position.x +=x;
    tetramino.position.y +=y;

    for b in tetramino.blocks:
        b.Transform.position.x += x * 0.5;
        b.Transform.position.y += y * 0.5;

def RotateTetramino(tetramino, CW):
    for b in tetramino.blocks:
        x = b.position.x
        y = b.position.y

        if (CW):
            b.position.x = tetramino.size - y - 1
            b.position.y = x
        else:
            b.position.y = tetramino.size - x - 1
            b.position.x = y

        b.Transform.position.x = b.position.x/2 + tetramino.position.x/2
        b.Transform.position.y = -b.position.y/2 + tetramino.position.y/2

def CheckFitTetramino(tetramino):
    collision2D()
    flag = True
    for b in tetramino.blocks:

        if (b.trigger):
            b.trigger = False
            flag = False

    return flag

def update():
    global currentTetra
    global speedCounter

    # create Tetramino If There Is None
    if (currentTetra == None):
        currentTetra = CreateTetramino(random.randint(0, 6))
        MoveTetramino(currentTetra, -5, 9)
        if not CheckFitTetramino(currentTetra):
            GameOver()

    #Input
    if (KeyDown["right"]):
        MoveTetramino(currentTetra, 1,0)
        if not CheckFitTetramino(currentTetra):
            MoveTetramino(currentTetra, -1, 0)
    if (KeyDown["left"]):
        MoveTetramino(currentTetra, -1,0)
        if not CheckFitTetramino(currentTetra):
            MoveTetramino(currentTetra, 1, 0)
    if (KeyDown["down"]):
        MoveTetramino(currentTetra, 0,-1)
        if not CheckFitTetramino(currentTetra):
            MoveTetramino(currentTetra, 0, 1)
    if (KeyDown["up"]):
        RotateTetramino(currentTetra,True)
        if not CheckFitTetramino(currentTetra):
            RotateTetramino(currentTetra,False)

    speedCounter += 1

    if (speedCounter >= speed):
        speedCounter = Variables.deltaTime

        # Move Tetramino Down
        MoveTetramino(currentTetra, 0, -1)
        if not CheckFitTetramino(currentTetra):
            MoveTetramino(currentTetra, 0, 1)
            #Clear Lines ???
            currentTetra = None

    pass


# Start
cam = GameObject()
cam.Camera = Camera()

blocks = [[None]*18]*10

#Walls
for i in range(0,18):
    newBlock1 = CreateBlock()
    newBlock2 = CreateBlock()

    newBlock1.Transform.position = Vector3D(-4.5,4.5 - i * 0.5,0)
    newBlock2.Transform.position = Vector3D(1,4.5 - i * 0.5,0)

#Floor
for i in range(0,12):
    newBlock = CreateBlock()
    newBlock.Transform.position = Vector3D(-4.5 + i * 0.5,-4.5,0)
currentTetra = None

speed = 20
speedCounter = 0

# Init
updateFunctions.append(update)
Main()
