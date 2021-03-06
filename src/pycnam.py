from typing import List

from PyQt5 import QtGui
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                            QGridLayout, QPushButton, QLabel,
                            QSizePolicy)
from PyQt5.QtCore import Qt

from characters import Ghost, Pacman
from map import GameMap
from game_manager import GameManager


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
        self.manager = GameManager(self.gameMap, self.ghosts)
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
        self.score.setStyleSheet('''
            color: #fff;
            font-size: 14px;
            font-weight: 500;
        ''')

        self.pacman = Pacman()
        self.ghosts = [Ghost('red'), Ghost('blue'), Ghost('green')]

        self.container = QVBoxLayout()
        self.container.addWidget(title)
        self.container.addWidget(self.score)
        self.container.addWidget(self.gameMap)
        self.container.addWidget(self.playButton)

        self.setStyleSheet('background-color: #000;')
        self.setLayout(self.container)
        self.setWindowTitle('Pycman')
        self.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        self.resize(500, 500)
        self.show()

    def initGame(self):
        self.gameMap.reset()
        self.manager = GameManager(self.gameMap, self.ghosts)
        self.setScore(0)
        y, x = self.manager.getPacmanPosition()
        startBlock = self.gameMap.mapWidgets[y][x]
        startBlock.visit()
        startBlock.hide()
        self.pacman.rotate('RIGHT')
        self.gameMap.mapLayout.addWidget(self.pacman, y, x)

        y, x = self.manager.getGhostPosition('red')
        self.gameMap.mapLayout.addWidget(self.ghosts[0], y, x)
        y, x = self.manager.getGhostPosition('blue')
        self.gameMap.mapLayout.addWidget(self.ghosts[1], y, x)
        y, x = self.manager.getGhostPosition('green')
        self.gameMap.mapLayout.addWidget(self.ghosts[2], y, x)

    def handlePlayClick(self):
        if self.manager.isPlaying():
            self.manager.stopGame()
            self.playButton.setText('Play Game')
        else:
            self.initGame()
            self.manager.startGame()
            self.playButton.setText('Stop Game')

    def setScore(self, score: int):
        self.score.setText(f'Score: {score}')

    def keyPressEvent(self, e: QtGui.QKeyEvent):
        if not self.manager.isPlaying():
            return

        key = e.key()
        y, x = self.manager.getPacmanPosition()

        if key == Qt.Key_Up:
            self.pacman.rotate('UP')
            self.manager.movePacmac(y - 1, x, self.pacman)
        elif key == Qt.Key_Down:
            self.pacman.rotate('DOWN')
            self.manager.movePacmac(y + 1, x, self.pacman)
        elif key == Qt.Key_Left:
            self.pacman.rotate('LEFT')
            self.manager.movePacmac(y, x - 1, self.pacman)
        elif key == Qt.Key_Right:
            self.pacman.rotate('RIGHT')
            self.manager.movePacmac(y, x + 1, self.pacman)
        self.setScore(self.manager.score)

    def closeEvent(self, a0: QtGui.QCloseEvent):
        self.manager.stopGame()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Pycman()
    sys.exit(app.exec_())
