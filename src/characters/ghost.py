from typing import Tuple
from PyQt5.QtWidgets import QWidget

class Ghost(QWidget):
    color: str
    position: Tuple

    def __init__(self, color, position):
        super().__init__()
        self.color = color
        self.position = position
        self.initCharacter()

    def initCharacter(self):
        if self.color == 'red':
            pass
        elif self.color == 'yellow':
            pass
        elif self.color == 'blue':
            pass

    def move(x, y):
        pass
