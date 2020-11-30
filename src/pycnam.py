from typing import List
from PyQt5.QtWidgets import (QApplication, QWidget,
                            QGridLayout, QPushButton)

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
        self.initGUI()
        self.initGame()
        self.manager = GameManager()

    def initGUI(self):
        self.playButton = QPushButton('Play Game')
        self.playButton.clicked.connect(self.handlePlayClick)
        self.container = QGridLayout()
        self.container.addWidget(self.playButton, 0, 0)
        self.setLayout(self.container)
        self.setWindowTitle('Pycman')
        self.setGeometry(100, 100, 500, 500)
        self.show()

    def initGame(self):
        pass

    def handlePlayClick(self):
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
