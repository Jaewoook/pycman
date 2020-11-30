from typing import Tuple
from PyQt5.QtWidgets import (QWidget, QGridLayout)

class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.initMap()

    def initMap(self):
        pass

class Block(QWidget):
    position: Tuple
    def __init__(self, position):
        super().__init__()
        self.position = position
