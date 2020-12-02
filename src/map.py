from typing import Tuple
from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QLabel, QSizePolicy)
from PyQt5.QtGui import QPalette, QPainter, QColor, QPen
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


class GameMap(QWidget):
    mapLayout: QGridLayout

    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.initMap()

    def initMap(self):
        container = QGridLayout()
        container.setSpacing(0)
        container.setHorizontalSpacing(0)
        container.setVerticalSpacing(0)
        for i, row in enumerate(PACMAN_MAP):
            for j, col in enumerate(row):
                block = Block(BLOCK_TYPE[col])
                container.addWidget(block, i, j)

        self.mapLayout = container
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.setLayout(self.mapLayout)
        self.setStyleSheet('background-color: #000;')
        self.show()

    def isWall(self, x: int, y: int):
        return PACMAN_MAP[x][y] != 'N'


class Block(QWidget):
    type: int

    def __init__(self, type):
        super().__init__()
        self.type = type
        layout = QVBoxLayout()
        layout.setSpacing(0)
        content = QLabel()
        content.setStyleSheet('color: #fff; background-color: #fff;')
        # layout.addWidget(content)
        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.show()

    def sizeHint(self):
        return QSize(25, 25)

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
        painter.drawLine(0, 11, 25, 11)

    def drawVWall(self, painter: QPainter):
        pen = QPen(Qt.white, 2, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(11, 0, 11, 25)

    def drawTWall(self, painter: QPainter):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 24, 25, 24)

    def drawBWall(self, painter: QPainter):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 1, 25, 1)

    def drawLWall(self, painter: QPainter):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(1, 0, 1, 25)

    def drawRWall(self, painter: QPainter):
        pen = QPen(Qt.white, 6, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(24, 0, 24, 25)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys
    app = QApplication(sys.argv)
    test = Map()
    test.setWindowTitle('Test')
    print(test.size().width(), test.size().height())
    sys.exit(app.exec_())
