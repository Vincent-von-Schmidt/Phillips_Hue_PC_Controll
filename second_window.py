from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget
from widgets import widgetButton, widgetLabel, widgetSlider, widgetTextEdit, widgetCheckBox
import format
import functions
import pyqt5_phillips_hue_widget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------------
        # config

        self.title = 'Phillips Hue PC Control v0.1.2'

        # screen size
        self.width = 1280
        self.height = 720

        # Phillips Hue
        self.hue_username = 'UoghabPi6o43qbmxud5U76fjgKF6BPtgznFCM-FT'
        self.hue_IP = '192.168.178.37'

        # --------------------------------------------------------------------

        # ui fixpoint
        self.CENTER = [self.width/2, self.height/2]

        self.text = widgetLabel.Text(
            widget=self,
            position=[self.CENTER[0], self.CENTER[1]],
            text="second screen",
            font_size=format.normal_font_size
        )

        self.switch_button = widgetButton.Button(
            widget=self,
            position=[self.CENTER[0], self.CENTER[1] + 100],
            text="switch button"
        )

        # activate the ui
        # self.init_ui()

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
