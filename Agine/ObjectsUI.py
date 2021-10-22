from .Attributes import  *

text = []
class Text(Attribute):
    def __init__(self, text = "New Text", fontSize = 24, color = [0,0,0]):
        self.text = text
        self.fontSize = fontSize
        self.color = color

button = []
class Button(Attribute):
    def __init__(self):
        self.onClick = []
        self.isInteractable = True
