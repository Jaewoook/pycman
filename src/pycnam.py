from typing import List
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                            QGridLayout, QPushButton, QLabel)

from characters.ghost import Ghost
from characters.pacman import Pacman
from map import Map
from game_manager import GameManager
import simple_ai

class Pycman(QWidget):
    manager: GameManager
    container: QGridLayout
    gameMap: Map
    ghosts: List[Ghost]
    pacman: Pacman

    playButton: QPushButton

    def __init__(self):
        super().__init__()
        self.manager = GameManager()
        self.initGUI()
        self.initGame()

    def initGUI(self):
        title = QLabel('Pycman Game')
        title.setStyleSheet('color: #fff; font-size: 20px;')
        self.gameMap = Map()
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
        self.container = QVBoxLayout()
        # self.container.addWidget(title)
        self.container.addWidget(self.gameMap)
        self.container.addWidget(self.playButton)
        self.setStyleSheet('background-color: #000;')
        self.setLayout(self.container)
        self.setWindowTitle('Pycman')
        self.setGeometry(100, 100, 500, 500)
        self.show()

    def initGame(self):
        self.manager.resetGame()

    def handlePlayClick(self):
        print('play clicked')
        if self.manager.isPlaying():
            self.manager.stopGame()
            self.playButton.setText('Play Game')
        else:
            self.manager.startGame()
            self.playButton.setText('Stop Game')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Pycman()
    sys.exit(app.exec_())
