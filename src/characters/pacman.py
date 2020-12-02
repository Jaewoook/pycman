from os import path, getcwd

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5.QtCore import Qt


class Pacman(QWidget):
    originalImg: QPixmap
    img: QPixmap
    imgLabel: QLabel

    def __init__(self):
        super().__init__()
        self.initCharacter()

    def initCharacter(self):
        img = QPixmap(path.join(getcwd(), 'pacman.png'))
        self.originalImg = self.img = img.scaledToWidth(25)
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
        elif d == 'UP':
            transform.rotate(90)
        elif d == 'DOWN':
            transform.rotate(270)

        self.img = self.originalImg.transformed(transform, Qt.SmoothTransformation)
        self.imgLabel.setPixmap(self.img)
