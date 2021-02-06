from .Attributes import  *
from .Input import *

text = []
class Text(Attribute):
    def __init__(self, text = "New Text", fontSize = 24, color = [0,0,0]):
        self.text = text
        self.fontSize = fontSize
        self.color = color

button = []
class Button(Attribute):
    def __init__(self,onClick = [], color = [0,0,0]):
        self.onClick = onClick
        self.color = color
        self.isInteractable = True


def eventsUI():
    for cam in camera:
        newMousePos = cam.Camera.ScreenToWorldVector2D(mousePos)

        for obj in button:
            if obj.Transform2D.position.x - obj.Transform2D.scale.x / 2 < newMousePos.x < obj.Transform2D.position.x + obj.Transform2D.scale.x / 2 and obj.Transform2D.position.y - obj.Transform2D.scale.y / 2 < newMousePos.y < obj.Transform2D.position.y + obj.Transform2D.scale.y / 2:
                if MouseDown["button0"]:
                    for func in obj.Button.onClick:
                        func()
