from typing import List
import threading
from random import randint

from map import GameMap
from characters import Pacman, Ghost


def randomMove():
    return randint(-1, 1), randint(-1, 1)


class GameManager:
    looper: threading.Timer
    playing: bool
    score: int
    pacmanPos: List[int]
    ghostsPos: List[List[int]]

    map: GameMap
    ghosts: List[Ghost]

    def __init__(self, gameMap: GameMap, ghosts: List[Ghost]):
        self.looper = None
        self.playing = False
        self.score = 0
        self.map = gameMap
        self.ghosts = ghosts
        self.pacmanPos = [9, 1]
        self.ghostsPos = [[5, 4], [5, 5], [5, 6]]

    def loop(self):
        self.looper = threading.Timer(0.5, self.loop)
        self.moveGhosts()
        self.looper.start()

    def resetGame(self):
        self.looper = None
        self.playing = False
        self.score = 0
        self.pacmanPos = [9, 1]
        self.ghostsPos = [[5, 4], [5, 5], [5, 6]]

    def startGame(self):
        self.playing = True
        self.looper = threading.Timer(0.5, self.loop)
        self.looper.start()

    def stopGame(self):
        self.playing = False
        self.map.ready = False
        if self.looper is not None:
            self.looper.cancel()

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

    def updateGhostPosition(self, idx: int, y: int, x: int):
        self.ghostsPos[idx] = [y, x]

    def movePacmac(self, y: int, x: int, pacman: Pacman):
        if self.map.isWall(y, x):
            return

        oldY, oldX = self.pacmanPos

        self.map.mapLayout.removeWidget(pacman)
        nextBlock = self.map.mapWidgets[y][x]
        if nextBlock.visit():
            self.score += 1
        nextBlock.hide()

        self.map.mapWidgets[oldY][oldX].show()
        self.map.mapLayout.addWidget(pacman, y, x)

        self.updatePacmanPosition(y, x)

    def moveGhosts(self):
        if not self.isPlaying():
            return

        for i in range(0, len(self.ghosts)):
            deltaY, deltaX = randomMove()
            oldY, oldX = self.ghostsPos[i]
            ghost = self.ghosts[i]
            self.map.mapLayout.removeWidget(ghost)
            x = oldX + deltaX
            y = oldY + deltaY
            if self.map.isWall(y, x):
                continue
            if oldY != y or oldX != x:
                self.map.mapLayout.addWidget(ghost, y, x)
                self.updateGhostPosition(i, y, x)
