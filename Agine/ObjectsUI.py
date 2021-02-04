from .Attributes import  Attribute

text = []
class Text(Attribute):
    def __init__(self, text = "New Text", color = [0,0,0]):
        self.text = text
        self.color = color

button = []
class Button(Attribute):
    def __init__(self, onClick = [], color = [0,0,0]):
        self.onClick = onClick
        self.color = color
        self.isInteractable = True



objectsUI = []