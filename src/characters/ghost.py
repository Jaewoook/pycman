from os import path, getcwd

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt


class Ghost(QWidget):
    originalImg: QPixmap
    img: QPixmap
    imgLabel: QLabel

    def __init__(self, color: str):
        super().__init__()
        self.initCharacter(color)

    def initCharacter(self, color):
        imgPath = path.join(getcwd(), 'images/ghost')
        if color == 'red':
            imgPath += '_red.png'
        elif color == 'blue':
            imgPath += '_blue.png'
        self.originalImg = self.img = QPixmap(imgPath)
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(self.img)
        self.imgLabel.setStyleSheet('background: transparent;')
        self.imgLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(self.imgLabel)
        self.setLayout(layout)

    def rotate(self, d: str):
        transform = QTransform()
        if d == 'LEFT':
            transform.rotate(0)
        elif d == 'RIGHT':
            transform.rotate(180)

        self.img = self.originalImg.transformed(transform, Qt.SmoothTransformation)
        self.imgLabel.setPixmap(self.img)
