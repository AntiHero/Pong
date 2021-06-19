from rectangle import Rectangle

class Paddle(Rectangle):
    def __init__(self):
        super().__init__(width=800, height=600, color=(0, 0, 0))