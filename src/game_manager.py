class GameManager:
    playing: bool

    def __init__(self):
        self.playing = False

    def startGame(self):
        self.playing = True

    def stopGame(self):
        self.playing = False

    def isPlaying(self):
        return self.playing
