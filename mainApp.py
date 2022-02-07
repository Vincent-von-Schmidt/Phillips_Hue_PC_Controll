from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QMainWindow
from widgets import widgetButton, widgetLabel, widgetSlider, widgetTextEdit, widgetCheckBox
import format
import functions
import pyqt5_phillips_hue_widget
import second_window


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

        self.panel_one = pyqt5_phillips_hue_widget.PhillipsHuePanel(
            widget=self,
            position=self.CENTER,
            light=3,
            hue_ip=self.hue_IP,
            name="lightstrip",
            hue_user=self.hue_username
        )
        self.panel_one.set_current_state()

        self.panel_two = pyqt5_phillips_hue_widget.PhillipsHuePanel(
            widget=self,
            position=[self.CENTER[0] - 250, self.CENTER[1]],
            light=1,
            hue_ip=self.hue_IP,
            hue_user=self.hue_username
        )
        self.panel_two.set_current_state()

        self.panel_three = pyqt5_phillips_hue_widget.PhillipsHuePanel(
            widget=self,
            position=[self.CENTER[0] + 250, self.CENTER[1]],
            light=14,
            hue_ip=self.hue_IP,
            hue_user=self.hue_username,
            name="PC passive"
        )
        self.panel_three.set_current_state()

        self.switch_button = widgetButton.Button(
            widget=self,
            text="switch window",
            position=[self.CENTER[0] - 450, self.CENTER[1] - 250],
            on_click=lambda: second_window.show()
        )

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
