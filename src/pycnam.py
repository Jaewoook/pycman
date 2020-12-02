from typing import List
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                            QGridLayout, QPushButton, QLabel,
                            QSizePolicy)
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtCore import Qt

from characters import Ghost, Pacman
from map import GameMap
from game_manager import GameManager
import simple_ai


class Pycman(QWidget):
    manager: GameManager
    container: QGridLayout
    gameMap: GameMap
    ghosts: List[Ghost]
    pacman: Pacman

    playButton: QPushButton
    score: QLabel

    def __init__(self):
        super().__init__()
        self.initGUI()
        self.initGame()

    def initGUI(self):
        title = QLabel('Pycman Game')
        title.setStyleSheet('color: #fff; font-size: 20px;')
        self.gameMap = GameMap()
        self.playButton = QPushButton('Play Game')
        self.playButton.setStyleSheet('''
            width: 100%;
            text-align: center;
            padding: 10px 0;
            border-width: 2px;
            border-style: dashed;
            border-color: #ff0;
            border-radius: 2px;
            color: #ff0;
        ''')
        self.playButton.clicked.connect(self.handlePlayClick)

        self.score = QLabel()
        self.setScore(0)
        self.score.setStyleSheet('''
            color: #fff;
            font-size: 14px;
            font-weight: 500;
        ''')

        self.pacman = Pacman()

        self.container = QVBoxLayout()
        self.container.addWidget(title)
        self.container.addWidget(self.score)
        self.container.addWidget(self.gameMap)
        self.container.addWidget(self.playButton)
        # self.container.addWidget(self.pacman)

        self.setStyleSheet('background-color: #222;')
        self.setLayout(self.container)
        self.setWindowTitle('Pycman')
        # self.setGeometry(100, 100, 500, 500)
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.resize(500, 500)
        self.show()
        print(self.size().width(), self.size().height())

    def initGame(self):
        self.manager = GameManager(self.gameMap)
        x, y = self.manager.getPacmanPosition()
        self.gameMap.mapLayout.removeWidget(self.gameMap.mapLayout.itemAtPosition(x, y).widget())
        self.gameMap.mapLayout.addWidget(self.pacman, x, y)
        print('pacman:', self.pacman.size().width(), self.pacman.size().height())

    def handlePlayClick(self):
        print('play clicked')
        if self.manager.isPlaying():
            self.manager.stopGame()
            self.playButton.setText('Play Game')
        else:
            self.manager.startGame()
            self.playButton.setText('Stop Game')

    def setScore(self, score: int):
        self.score.setText(f'Score: {score}')

    def keyPressEvent(self, e: QKeyEvent):
        key = e.key()
        x, y = self.manager.getPacmanPosition()

        if key == Qt.Key_Up:
            self.manager.movePacmac(x - 1, y, self.pacman)
        elif key == Qt.Key_Down:
            self.manager.movePacmac(x + 1, y, self.pacman)
        elif key == Qt.Key_Left:
            self.manager.movePacmac(x, y - 1, self.pacman)
        elif key == Qt.Key_Right:
            self.manager.movePacmac(x, y + 1, self.pacman)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Pycman()
    sys.exit(app.exec_())
