import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QGraphicsScene, QGraphicsEllipseItem, QGraphicsView
from PyQt5.uic import loadUi
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import random


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()

        loadUi("UI.ui", self)

        self.pushButton.clicked.connect(self.showCircle)

        self.scene = QGraphicsScene()
        self.graphicsView.setScene(self.scene)

    def showCircle(self):
        diameter = random.randint(10, 100)
        circle = QGraphicsEllipseItem(0, 0, diameter, diameter)
        circle.setBrush(QColor(Qt.yellow))
        self.scene.addItem(circle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
