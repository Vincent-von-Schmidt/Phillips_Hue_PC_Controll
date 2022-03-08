from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QStackedWidget, QApplication, QHBoxLayout
from widgets import widgetButton, widgetLabel, widgetSlider, widgetTextEdit, widgetCheckBox
import format
import functions
import pyqt5_phillips_hue_widget
import sys


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------------
        # config

        self.title = 'Phillips Hue PC Control v0.3'

        # screen size
        self.width = 1280
        self.height = 720

        # Phillips Hue
        self.hue_username = 'UoghabPi6o43qbmxud5U76fjgKF6BPtgznFCM-FT'
        self.hue_IP = '192.168.178.37'

        # --------------------------------------------------------------------

        # ui fixpoint
        self.CENTER = [self.width/2, self.height/2]

        self.layout = QHBoxLayout()

        self.panel_three = pyqt5_phillips_hue_widget.PhillipsHuePanel(
            widget=self,
            position=[self.CENTER[0] + 250, self.CENTER[1]],
            light=14,
            hue_ip=self.hue_IP,
            hue_user=self.hue_username,
            name="PC passive"
        )

        self.layout.addWidget(self.panel_three)
        
        self.panel_three.set_current_state()

        # activate the ui
        self.init_ui()

    def init_ui(self):

        # add a window title
        self.setWindowTitle(self.title)

        # set window icon
        # self.setWindowIcon()

        # set screen size
        self.resize(self.width, self.height)
        self.setMinimumSize(QSize(self.width, self.height))
        self.setMaximumSize(QSize(self.width, self.height))

        # let you display the ui in a window
        self.show()


if __name__ == '__main__':
    app = QApplication([sys.argv])
    ex = MainWidget()

    with open("style.css", "r") as file:
        app.setStyleSheet(file.read())

    # app.setStyleSheet(style.stylesheet)

    sys.exit(app.exec_())
