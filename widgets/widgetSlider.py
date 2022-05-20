from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt


class Slider:
    def __init__(
            self,
            widget: object,
            orientation: str,
            position: list = None,
            on_change = None,
            start: int or float = 0,
            stop: int or float = 100,
            state_identifier: str = None,
            tool_tip: str = None,
            style_identifier: str = None
    ):

        self.widget = widget
        self.orientation = orientation
        self.start = start
        self.stop = stop
        self.state_identifier = state_identifier
        self.toolTip = tool_tip

        # create slider object
        self.slider = QSlider(self.widget)

        # define the position of the slider
        if position is not None:
            self.set_position(position)

        # define start and stop of the slider
        self.slider.setMinimum(self.start)
        self.slider.setMaximum(self.stop)

        # set orientation
        if self.orientation == 'vertical':
            self.slider.setOrientation(Qt.Vertical)
        elif self.orientation == 'horizontal':
            self.slider.setOrientation(Qt.Horizontal)
        else:
            raise TypeError('Only vertical and horizontal sliders exist.')

        if self.toolTip is not None:
            self.set_tool_tip(self.toolTip)

        # set on_change action
        if on_change is not None:
            self.connect(on_change)

        if style_identifier is not None:
            self.set_style_identifier(style_identifier)

    def get_width(self) -> int:
        return self.slider.width()

    def get_height(self) -> int:
        return self.slider.height()

    def get_value(self) -> int:
        return self.slider.value()

    def connect(self, function) -> None:
        self.slider.valueChanged.connect(function)

    def set_position(self, position: list) -> None:
        position = [int(position[0] - self.get_width() // 2), int(position[1] - self.get_height() // 2)]
        self.slider.move(position[0], position[1])

    def set_slider_to_number(self, position):
        self.slider.setSliderPosition(position)

    def set_tool_tip(self, tool_tip):
        self.slider.setToolTip(tool_tip)

    def set_style_identifier(self, style_identifier) -> None:
        self.slider.setObjectName(style_identifier)
