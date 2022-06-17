from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QWidget, QStackedWidget
from widgets import widgetButton, widgetLabel, widgetSlider, widgetTextEdit, widgetCheckBox
import format
import functions
import pyqt5_phillips_hue_widget


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        # --------------------------------------------------------------------
        # config

        self.title = 'Phillips Hue PC Control v0.2.1'

        # screen size
        self.width = 1280
        self.height = 720

        # Phillips Hue
        self.hue_username = 'UoghabPi6o43qbmxud5U76fjgKF6BPtgznFCM-FT'
        self.hue_IP = '192.168.178.37'

        # --------------------------------------------------------------------

        # ui fixpoint
        self.CENTER = [self.width/2, self.height/2]

        # self.ip_input = widgetTextEdit.LineEdit(
        #     widget=self,
        #     position=[self.CENTER[0] - 500, self.CENTER[1] + 250],
        #     text=self.hue_IP,
        #     on_change=lambda: self.hue_IP.replace(self.hue_IP, self.ip_input.get_user_input()),
        #     alignment="center",
        #     length=300,
        #     placeholder_text="bridge ip"
        # )
        #
        # self.find_bridge_ip_button = widgetButton.Button(
        #     widget=self,
        #     text="find bridge",
        #     position=[self.CENTER[0] - 190, self.CENTER[1] + 250]
        # )
        #
        # self.user_input = widgetTextEdit.LineEdit(
        #     widget=self,
        #     position=[self.CENTER[0] - 500, self.CENTER[1] + 300],
        #     text=self.hue_username,
        #     on_change=lambda: functions.combine_functions(
        #         self.hue_username.replace(self.hue_username, self.user_input.get_user_input()),
        #         print(self.hue_username)
        #     ),
        #     alignment="center",
        #     length=300,
        #     placeholder_text="user name"
        # )
        #
        # self.create_new_user_button = widgetButton.Button(
        #     widget=self,
        #     text="create new",
        #     position=[self.CENTER[0] - 190, self.CENTER[1] + 300]
        # )
        #
        # self.settings_button = widgetButton.Button(
        #     widget=self,
        #     position=[self.CENTER[0] - 580, self.CENTER[1] + 345],
        #     text="settings"
        # )

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
            light=15,
            hue_ip=self.hue_IP,
            hue_user=self.hue_username,
            name="bed"
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
