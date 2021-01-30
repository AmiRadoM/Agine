


class Text():
    def __init__(self, name = "", text = "New Text", position = [0,0]):
        self.name = name
        self.text = text
        self.x = position[0]
        self.y = position[1]
        SpritesUI.append(self)



SpritesUI = []