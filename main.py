from mainApp import MainWidget
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == '__main__':
    app = QApplication([sys.argv])
    ex = MainWidget()

    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())

    sys.exit(app.exec_())
