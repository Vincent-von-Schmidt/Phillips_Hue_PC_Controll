from mainApp import MainWidget
from PyQt5.QtWidgets import QApplication
import sys
import style

if __name__ == '__main__':
    app = QApplication([sys.argv])
    ex = MainWidget()

    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())

    # app.setStyleSheet(style.stylesheet)

    sys.exit(app.exec_())
