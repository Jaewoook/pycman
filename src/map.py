from typing import List
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QLabel, QSizePolicy)
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt, QSize

BLOCK_TYPE = {
    'EMPTY': -1,
    'N': 0,
    'L': 1,
    'R': 2,
    'T': 3,
    'B': 4,
    'H': 5,
    'V': 6,
}
PACMAN_MAP = [
    ['T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T', 'T'],
    ['L', 'N', 'N', 'N', 'N', 'V', 'N', 'N', 'N', 'N', 'R'],
    ['L', 'N', 'H', 'H', 'N', 'V', 'N', 'H', 'H', 'N', 'R'],
    ['L', 'N', 'V', 'N', 'N', 'N', 'N', 'N', 'V', 'N', 'R'],
    ['L', 'N', 'V', 'N', 'H', 'H', 'H', 'N', 'V', 'N', 'R'],
    ['L', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'R'],
    ['L', 'N', 'N', 'N', 'H', 'H', 'H', 'N', 'N', 'N', 'R'],
    ['L', 'N', 'V', 'N', 'N', 'N', 'N', 'N', 'V', 'N', 'R'],
    ['L', 'N', 'H', 'H', 'N', 'V', 'N', 'H', 'H', 'N', 'R'],
    ['L', 'N', 'N', 'N', 'N', 'V', 'N', 'N', 'N', 'N', 'R'],
    ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
]


class Block(QWidget):
    type: int
    painter: QPainter

    def __init__(self, blockType):
        super().__init__()
        self.type = blockType
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def sizeHint(self):
        return QSize(25, 25)

    def paintEvent(self, event):
        self.painter = QPainter()
        self.painter.begin(self)
        self.painter.eraseRect(event.rect())
        if self.type == -1:
            self.drawEmpty()
        elif self.type == 0:
            self.drawDot()
        elif self.type == 1:
            self.drawLWall()
        elif self.type == 2:
            self.drawRWall()
        elif self.type == 3:
            self.drawTWall()
        elif self.type == 4:
            self.drawBWall()
        elif self.type == 5:
            self.drawHWall()
        elif self.type == 6:
            self.drawVWall()
        self.painter.end()

    def drawEmpty(self):
        pen = QPen(Qt.black, 3)
        self.painter.setPen(pen)
        self.painter.drawPoint(11, 11)

    def drawDot(self):
        pen = QPen(Qt.yellow, 3)
        self.painter.setPen(pen)
        self.painter.drawPoint(11, 11)

    def drawHWall(self):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(0, 11, 25, 11)

    def drawVWall(self):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(11, 0, 11, 25)

    def drawTWall(self):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(0, 24, 25, 24)

    def drawBWall(self):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(0, 1, 25, 1)

    def drawLWall(self):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(1, 0, 1, 25)

    def drawRWall(self):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        self.painter.setPen(pen)
        self.painter.drawLine(24, 0, 24, 25)


class Cell(QWidget):
    visited: bool
    block: Block

    def __init__(self, blockType):
        super().__init__()
        self.visited = False if blockType >= 0 else True
        self.block = Block(blockType)
        layout = QVBoxLayout()
        layout.addWidget(self.block)
        layout.setSpacing(0)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.setLayout(layout)

    def sizeHint(self):
        return QSize(25, 25)

    def visit(self):
        if self.visited:
            return False
        self.visited = True
        self.block.type = -1
        self.block.update()
        return True

    def reset(self):
        self.show()
        if self.block.type == -1:
            self.visited = False
            self.block.type = 0
            self.block.update()


class GameMap(QWidget):
    mapLayout: QGridLayout
    mapWidgets: List[List[Cell]]
    ready: bool

    def __init__(self):
        super().__init__()
        self.ready = False
        self.initMap()

    def initMap(self):
        self.mapWidgets = []
        container = QGridLayout()
        container.setSpacing(0)
        container.setHorizontalSpacing(0)
        container.setVerticalSpacing(0)
        for i, row in enumerate(PACMAN_MAP):
            self.mapWidgets.append([])
            for j, col in enumerate(row):
                cell = Cell(BLOCK_TYPE[col])
                container.addWidget(cell, i, j)
                self.mapWidgets[i].append(cell)

        self.mapLayout = container
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setLayout(self.mapLayout)
        self.ready = True

    def isWall(self, y: int, x: int):
        return PACMAN_MAP[y][x] != 'N'

    def reset(self):
        if self.ready:
            return

        for row in self.mapWidgets:
            for cell in row:
                cell.reset()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    test = GameMap()
    test.setWindowTitle('Test')
    print(test.size().width(), test.size().height())
    sys.exit(app.exec_())
