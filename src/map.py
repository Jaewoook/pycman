from typing import Tuple
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QLabel)

BLANK = 0
WALL = {
    'V': 1,
    'H': 2,
}
PACMAN_MAP = [
    [WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['V'], BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, BLANK, WALL['V']],
    [WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H'], WALL['H']],
]

class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.initMap()

    def initMap(self):
        container = QGridLayout()
        for i, row in enumerate(PACMAN_MAP):
            for j, col in enumerate(row):
                block = Block(col, (i, j))
                container.addWidget(block, i, j)
        self.setLayout(container)
        self.show()


class Block(QWidget):
    position: Tuple
    type: int
    visited: bool
    def __init__(self, type, position, visited=False):
        super().__init__()
        self.type = type
        self.position = position
        self.visited = visited
        self.resize(25, 25)
        layout = QVBoxLayout()
        content = QLabel()
        content.setStyleSheet('color: #fff')
        if type == 0:
            content.setText('·')
        elif type == 1:
            content.setText('|')
        elif type == 2:
            content.setText('―')
        layout.addWidget(content)
        self.setLayout(layout)
        self.show()

    def markVisited(self):
        self.visited = True
