from typing import Tuple
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QLabel, QSizePolicy)
from PyQt5.QtGui import QPalette, QPainter, QColor, QPen
from PyQt5.QtCore import Qt

MAP_INFO = {
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

class Map(QWidget):
    def __init__(self):
        super().__init__()
        self.initMap()

    def initMap(self):
        container = QGridLayout()
        container.setHorizontalSpacing(0)
        container.setVerticalSpacing(0)
        for i, row in enumerate(PACMAN_MAP):
            for j, col in enumerate(row):
                block = Block(MAP_INFO[col], (i, j))
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
        layout = QVBoxLayout()
        layout.setSpacing(0)
        content = QLabel()
        content.setStyleSheet('color: #fff; background-color: #fff;')
        # layout.addWidget(content)
        self.resize(25, 25)
        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.show()

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        if self.type == 0:
            self.drawDot(painter)
        elif self.type == 1:
            self.drawLWall(painter)
        elif self.type == 2:
            self.drawRWall(painter)
        elif self.type == 3:
            self.drawTWall(painter)
        elif self.type == 4:
            self.drawBWall(painter)
        elif self.type == 5:
            self.drawHWall(painter)
        elif self.type == 6:
            self.drawVWall(painter)
        painter.end()


    def drawDot(self, painter: QPainter):
        pen = QPen(Qt.yellow, 3)
        painter.setPen(pen)
        painter.drawPoint(11, 11)

    def drawHWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 11, 23, 11)

    def drawTWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 23, 25, 23)

    def drawBWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 1, 25, 1)

    def drawLWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(1, 0, 1, 25)

    def drawRWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(23, 0, 23, 25)

    def drawVWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(11, 0, 11, 23)


    def markVisited(self):
        self.visited = True

if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    test = Map()
    test.setWindowTitle('Test')
    sys.exit(app.exec_())
