from os import path, getcwd

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QSizePolicy
from PyQt5.QtGui import QPixmap


class Pacman(QWidget):
    img: QPixmap
    imgLabel: QLabel

    def __init__(self):
        super().__init__()
        self.initCharacter()

    def initCharacter(self):
        img = QPixmap(path.join(getcwd(), 'pacman.png'))
        self.img = img.scaledToWidth(16)
        self.imgLabel = QLabel()
        self.imgLabel.setPixmap(self.img)
        self.imgLabel.setStyleSheet('background: transparent;')
        self.imgLabel.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        layout = QVBoxLayout()
        layout.setSpacing(0)
        layout.addWidget(self.imgLabel)
        self.setLayout(layout)

    def rotate(self, x: int, y: int):
        pass
