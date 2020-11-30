from typing import Tuple
from PyQt5.QtWidgets import QWidget

class Pacman(QWidget):
    position: Tuple

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.initCharacter()

    def initCharacter(self):
        pass

    def move(x: int, y: int):
        pass
