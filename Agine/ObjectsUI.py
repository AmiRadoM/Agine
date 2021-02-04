from .Attributes import  *
from .Input import *

text = []
class Text(Attribute):
    def __init__(self, text = "New Text", color = [0,0,0]):
        self.text = text
        self.color = color

button = []
class Button(Attribute):
    def __init__(self,onClick = [], color = [0,0,0]):
        self.onClick = onClick
        self.color = color
        self.isInteractable = True


def eventsUI():
    for cam in camera:
        from .Agine_main import gameDisplay
        newMousePos = mousePos / ((gameDisplay.scale / 2) / cam.Camera.scale)

        for obj in button:

            if obj.Transform2D.position.x - obj.Transform2D.scale.x / 2 < newMousePos.x < obj.Transform2D.position.x + obj.Transform2D.scale.x / 2 and obj.Transform2D.position.y - obj.Transform2D.scale.y / 2 < newMousePos.y < obj.Transform2D.position.y + obj.Transform2D.scale.y / 2:
                if MouseDown["button0"]:
                    for func in obj.Button.onClick:
                        func()
