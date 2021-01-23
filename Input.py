import pygame

class __mousePos():
    def __init__(self):
        self.x = 0
        self.y = 0

    def toList(self):
        return [self.x, self.y]

mousePos = __mousePos()

def input():
    from Agine_main import gameDisplay, cameraPos
    mousePos.x = pygame.mouse.get_pos()[0] - gameDisplay.display.get_width() / 2 + cameraPos[0]
    mousePos.y = -pygame.mouse.get_pos()[1]  + gameDisplay.display.get_width() / 2 + cameraPos[0]