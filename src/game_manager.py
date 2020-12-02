from typing import List

from map import GameMap, Cell, BLOCK_TYPE
from characters import Pacman


class GameManager:
    playing: bool
    score: int
    pacmanPos: List[int]
    ghostsPos: List[List[int]]

    map: GameMap

    def __init__(self, gameMap: GameMap = None):
        self.playing = False
        self.score = 0
        self.map = gameMap
        self.pacmanPos = [9, 1]
        self.ghostsPos = [[5, 4], [5, 5], [5, 6]]

    def startGame(self):
        self.playing = True

    def stopGame(self):
        self.playing = False

    def isPlaying(self):
        return self.playing

    def getPacmanPosition(self):
        return tuple(self.pacmanPos)

    def getGhostPosition(self, color: str):
        if color == 'red':
            return tuple(self.ghostsPos[0])
        elif color == 'blue':
            return tuple(self.ghostsPos[1])
        elif color == 'green':
            return tuple(self.ghostsPos[2])

    def updatePacmanPosition(self, y: int, x: int):
        self.pacmanPos = [y, x]

    def updateGhostPosition(self, color: str, y: int, x: int):
        idx = 0
        if color == 'red':
            idx = 0
        elif color == 'blue':
            idx = 1
        elif color == 'green':
            idx = 2
        self.ghostsPos[idx] = [y, x]

    def movePacmac(self, y: int, x: int, pacman: Pacman):
        if self.map.isWall(y, x):
            return

        oldY, oldX = self.pacmanPos

        self.map.mapLayout.removeWidget(pacman)
        nextBlock = self.map.mapWidgets[y][x]
        nextBlock.visit()
        nextBlock.hide()

        self.map.mapWidgets[oldY][oldX].show()
        self.map.mapLayout.addWidget(pacman, y, x)

        self.updatePacmanPosition(y, x)

