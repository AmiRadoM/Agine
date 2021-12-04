from Agine import *

def clamp(value, minValue, maxValue):
    return max(minValue, min(value, maxValue))

# class Piece(GameObject):
#     def __init__(self, piece = 1, color = 1):
#         super().__init__()
#         self.layer = 1
#         self.piece = piece #Pawn = 1, Knight = 2, Bishop = 3, Rook = 4, Queen = 5, King = 6
#         self.color = color; #white = 1, black = 2
#         self.followMouse = False
#         self.Sprite = Sprite()
#         self.Button = Button()
#         self.Button.onClick.append(lambda a: self.SetFollowMouse(True))
#         objects.append(self)
#
#     def SetFollowMouse(self, b):
#         self.followMouse = b

class Piece():
    def __init__(self, piece=1, color=1):
        self.piece = piece  # Pawn = 1, Knight = 2, Bishop = 3, Rook = 4, Queen = 5, King = 6
        self.color = color;  # white = 1, black = 0
        self.followMouse = False


def MovePiece(i,j,x,y):
    board[i][j].Transform.position = Vector3D(x, y, 0)
    piece = board[i][j]
    replacedPiece = board[x][y]
    board[x][y] = piece
    if (type(replacedPiece) == GameObject):
        replacedPiece.Delete()
    board[i][j] = None

def PieceClick(piece):
    global firstLocationW
    global lastLocationW
    global firstLocationB
    global lastLocationB

    if turn == piece.Piece.color:
        piece.Piece.followMouse = True
        if (turn == 1):
            if (type(firstLocationW) == GameObject):
                firstLocationW.Delete()
            if (type(lastLocationW) == GameObject):
                firstLocationW.Delete()
            firstLocationW = location.Create()
            firstLocationW.isVisible = False
            firstLocationW.Transform.position = piece.Transform.position
            firstLocationW.Square.color = locationColorW
        else:
            if (type(firstLocationB) == GameObject):
                firstLocationB.Delete()
            if (type(lastLocationB) == GameObject):
                firstLocationB.Delete()
            firstLocationB = location.Create()
            firstLocationB.isVisible = False
            firstLocationB.Transform.position = piece.Transform.position
            firstLocationB.Square.color = locationColorB

def CreatePiece(gObject,piece=1,color=1):
    newPiece = gObject.Create()
    newPiece.Piece.piece = piece
    newPiece.Piece.color = color
    return newPiece


def update():
    global board
    global turn
    global lastLocationB
    global lastLocationW

    for i in range(8):
        for j in range(8):
            if (board[i][j] != None):
                #Makes All Following Pieces follow the mouse
                if (board[i][j].Piece.followMouse):
                    board[i][j].Transform.position = cam.Camera.ScreenToWorldVector2D(mousePos)
                    board[i][j].layer = 3

    #Release All Following Mouse
    if (MouseUp["button0"]):
        for i in range(8):
            for j in range(8):
                if (board[i][j] != None):
                    if (board[i][j].Piece.followMouse):
                        board[i][j].layer = 2
                        board[i][j].Piece.followMouse = False
                        newX = clamp(round(board[i][j].Transform.position.x),0,7)
                        newY = clamp(round(board[i][j].Transform.position.y),0,7)
                        board[i][j].Transform.position = Vector3D(newX,newY,0)
                        if (i != newX or j != newY):    #If Put In New Position
                            MovePiece(i,j,newX,newY)
                            if (turn == 1):
                                firstLocationW.isVisible = True
                                lastLocationW = location.Create()
                                lastLocationW.Transform.position = Vector3D(newX,newY)
                                lastLocationW.Square.color = locationColorW
                                if (type(firstLocationB) == GameObject):
                                    firstLocationB.Delete()
                                if (type(lastLocationB) == GameObject):
                                    lastLocationB.Delete()
                            else:
                                firstLocationB.isVisible = True
                                lastLocationB = location.Create()
                                lastLocationB.Transform.position = Vector3D(newX, newY)
                                lastLocationB.Square.color = locationColorB
                                if (type(firstLocationW) == GameObject):
                                    firstLocationW.Delete()
                                if (type(lastLocationW) == GameObject):
                                    lastLocationW.Delete()
                            #Change color turn
                            turn = not turn
                        else:   # If In the Same Position
                            if (turn == 1):
                                firstLocationW.Delete()
                            else:
                                firstLocationB.Delete()




#Start
cam = GameObject()
cam.Camera = Camera()
cam.Transform.position = Vector3D(3.5,3.5,0)

turn = 1

location = GameObject()
location.DontRender()
location.layer = 1
location.Square = Square()

firstLocationW = None
lastLocationW = None
locationColorW = [208,239,255]

firstLocationB = None
lastLocationB = None
locationColorB = [255,139,142]

board = [[None]*8 for i in range(8)]

piece = GameObject()
piece.layer = 2
piece.Piece = Piece()
piece.Sprite = Sprite()
piece.Button = Button()
piece.Button.onClick.append(lambda a: PieceClick(a))

#Create Board
for i in range(4):
    for j in range(8):
        blackSqr = GameObject()
        whiteSqr = GameObject()
        blackSqr.Square = Square()
        whiteSqr.Square = Square()
        blackSqr.Square.color = [101,67,33]
        whiteSqr.Square.color = [244,226,198]
        blackSqr.Transform.position = Vector3D(i * 2 + j % 2,j,0)
        whiteSqr.Transform.position = Vector3D(i * 2 - j % 2 + 1,j,0)

#Set Pieces
#Pawns
for i in range(8):
    board[i][1] = CreatePiece(piece,1,1)
    board[i][6] = CreatePiece(piece,1,0)
#Knights
board[1][0] = CreatePiece(piece,2,1)
board[6][0] = CreatePiece(piece,2,1)
board[1][7] = CreatePiece(piece,2,0)
board[6][7] = CreatePiece(piece,2,0)
#Bishops
board[2][0] = CreatePiece(piece,3,1)
board[5][0] = CreatePiece(piece,3,1)
board[2][7] = CreatePiece(piece,3,0)
board[5][7] = CreatePiece(piece,3,0)
#Rooks
board[0][0] = CreatePiece(piece,4,1)
board[7][0] = CreatePiece(piece,4,1)
board[0][7] = CreatePiece(piece,4,0)
board[7][7] = CreatePiece(piece,4,0)
#Queens
board[3][0] = CreatePiece(piece,5,1)
board[3][7] = CreatePiece(piece,5,0)
#Kings
board[4][0] = CreatePiece(piece,6,1)
board[4][7] = CreatePiece(piece,6,0)

#Place Pieces
for i in range(8):
    for j in range(8):
        if (board[i][j] != None):
            board[i][j].Transform.position = Vector3D(i,j,0)
            if(board[i][j].Piece.piece == 1):
                board[i][j].Sprite.imagePath = "./Pieces/Pawn" +( "W" if (board[i][j].Piece.color == 1) else "B") + ".png"
            if (board[i][j].Piece.piece == 2):
                board[i][j].Sprite.imagePath = "./Pieces/Knight" + ("W" if (board[i][j].Piece.color == 1) else "B") + ".png"
            if (board[i][j].Piece.piece == 3):
                board[i][j].Sprite.imagePath = "./Pieces/Bishop" + ("W" if (board[i][j].Piece.color == 1) else "B") + ".png"
            if (board[i][j].Piece.piece == 4):
                board[i][j].Sprite.imagePath = "./Pieces/Rook" + ("W" if (board[i][j].Piece.color == 1) else "B") + ".png"
            if (board[i][j].Piece.piece == 5):
                board[i][j].Sprite.imagePath = "./Pieces/Queen" + ("W" if (board[i][j].Piece.color == 1) else "B") + ".png"
            if (board[i][j].Piece.piece == 6):
                board[i][j].Sprite.imagePath = "./Pieces/King" + ("W" if (board[i][j].Piece.color == 1) else "B") + ".png"



#Init
updateFunctions.append(update)
Main()