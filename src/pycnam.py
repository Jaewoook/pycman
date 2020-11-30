from PyQt5.QtWidgets import QApplication, QWidget

class Pycman(QWidget):
    def __init__(self):
        super().__init__()
        self.initGUI()

    def initGUI(self):
        self.setWindowTitle('Pycman')
        self.setGeometry(200, 200, 500, 500)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    game = Pycman()
    sys.exit(app.exec_())
