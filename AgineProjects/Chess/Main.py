from Agine import *

def clamp(value, minValue, maxValue):
    return max(minValue, min(value, maxValue))

class Piece(GameObject):
    def __init__(self, piece = 1, color = 1):
        super().__init__()
        self.layer = 1
        self.piece = piece #Pawn = 1, Knight = 2, Bishop = 3, Rook = 4, Queen = 5, King = 6
        self.color = color; #whitte = 1, black = 2
        self.followMouse = False
        self.Sprite = Sprite()
        self.Button = Button()
        self.Button.onClick.append(lambda a: self.SetFollowMouse(True))

    def __del__(self):
        objects.remove(self)
    
    def SetFollowMouse(self, b):
        self.followMouse = b
        print("A")


def update():
    global board

    for i in range(8):
        for j in range(8):
            if (board[i][j] != None):
                #Makes All Following Pieces follow the mouse
                if (board[i][j].followMouse):
                    board[i][j].Transform.position = cam.Camera.ScreenToWorldVector2D(mousePos)

    #Release All Following Mouse
    if (MouseUp["button0"]):
        for i in range(8):
            for j in range(8):
                if (board[i][j] != None):
                    if (board[i][j].followMouse):
                        board[i][j].followMouse = False
                        newX = clamp(round(board[i][j].Transform.position.x),0,7)
                        newY = clamp(round(board[i][j].Transform.position.y),0,7)
                        board[i][j].Transform.position = Vector3D(newX,newY,0)
                        if (i != newX or j != newY):
                            piece = board[i][j]
                            del (board[newX][newY])
                            board[newX].insert(newY, piece)
                            del (board[i][j])
                            board[i].insert(j, None)




#Start
cam = GameObject()
cam.Camera = Camera()
cam.Transform.position = Vector3D(3.5,3.5,0)

board = [[None]*8 for i in range(8)]

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
    board[i][1] = Piece(1,1)
    board[i][6] = Piece(1,2)
#Knights
board[1][0] = Piece(2,1)
board[6][0] = Piece(2,1)
board[1][7] = Piece(2,2)
board[6][7] = Piece(2,2)
#Bishops
board[2][0] = Piece(3,1)
board[5][0] = Piece(3,1)
board[2][7] = Piece(3,2)
board[5][7] = Piece(3,2)
#Rooks
board[0][0] = Piece(4,1)
board[7][0] = Piece(4,1)
board[0][7] = Piece(4,2)
board[7][7] = Piece(4,2)
#Queens
board[3][0] = Piece(5,1)
board[3][7] = Piece(5,2)
#Kings
board[4][0] = Piece(6,1)
board[4][7] = Piece(6,2)

#Place Pieces
for i in range(8):
    for j in range(8):
        if (board[i][j] != None):
            board[i][j].Transform.position = Vector3D(i,j,0)
            if(board[i][j].piece == 1):
                board[i][j].Sprite.imagePath = "./Pieces/Pawn" +( "W" if (board[i][j].color == 1) else "B") + ".png"
            if (board[i][j].piece == 2):
                board[i][j].Sprite.imagePath = "./Pieces/Knight" + ("W" if (board[i][j].color == 1) else "B") + ".png"
            if (board[i][j].piece == 3):
                board[i][j].Sprite.imagePath = "./Pieces/Bishop" + ("W" if (board[i][j].color == 1) else "B") + ".png"
            if (board[i][j].piece == 4):
                board[i][j].Sprite.imagePath = "./Pieces/Rook" + ("W" if (board[i][j].color == 1) else "B") + ".png"
            if (board[i][j].piece == 5):
                board[i][j].Sprite.imagePath = "./Pieces/Queen" + ("W" if (board[i][j].color == 1) else "B") + ".png"
            if (board[i][j].piece == 6):
                board[i][j].Sprite.imagePath = "./Pieces/King" + ("W" if (board[i][j].color == 1) else "B") + ".png"



#Init
updateFunctions.append(update)
Main()