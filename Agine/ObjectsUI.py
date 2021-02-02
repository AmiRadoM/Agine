from .Attributes import  Attribute


class Text(Attribute):
    def __init__(self, text = "New Text", fontPath = ""):
        self.text = text
        self.fontPath = fontPath



objectsUI = []