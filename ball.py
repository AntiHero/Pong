from rectangle import Rectangle

class Ball(Rectangle):
    def __init__(self, width, height, color):
        super().__init__(width=20, height=20, color=(0, 0, 0))