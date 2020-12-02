from typing import List

from map import GameMap, Block, BLOCK_TYPE
from characters import Pacman

class GameManager:
    playing: bool
    score: int
    pacmanPos: List[int]

    map: GameMap

    def __init__(self, gameMap: GameMap = None):
        self.playing = False
        self.score = 0
        self.map = gameMap
        self.pacmanPos = [9, 1]

    def startGame(self):
        self.playing = True

    def stopGame(self):
        self.playing = False

    def isPlaying(self):
        return self.playing

    def getPacmanPosition(self):
        return tuple(self.pacmanPos)

    def updatePacmanPosition(self, x: int, y: int):
        self.pacmanPos = [x, y]

    def movePacmac(self, x: int, y: int, pacman: Pacman):
        if self.map.isWall(x, y):
            return

        oldX, oldY = self.pacmanPos

        pacman = self.map.mapLayout.itemAtPosition(oldX, oldY).widget()
        self.map.mapLayout.removeWidget(pacman)
        emptyBlock = Block(BLOCK_TYPE['EMPTY'])
        self.map.mapLayout.addWidget(emptyBlock, oldX, oldY)

        nextBlock = self.map.mapLayout.itemAtPosition(x, y).widget()
        self.map.mapLayout.removeWidget(nextBlock)
        self.map.mapLayout.addWidget(pacman, x, y)

        self.updatePacmanPosition(x, y)

