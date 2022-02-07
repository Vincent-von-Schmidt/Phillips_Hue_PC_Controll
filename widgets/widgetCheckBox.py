from PyQt5.QtWidgets import QCheckBox


class CheckBox:
    def __init__(self, widget, position, text, toolTip=None):
        self.widget = widget
        self.position = position
        self.text = text
        self.toolTip = toolTip

        # create object
        self.checkBox = QCheckBox(self.widget)

        # set position
        self.checkBox.move(self.position[0], self.position[1])

        # set text
        self.checkBox.setText(self.text)

        # set toolTip
        if self.toolTip is not None:
            self.checkBox.setToolTip(self.toolTip)

    def connect(self, function):
        self.checkBox.clicked.connect(function)

    def get_value(self):
        return self.checkBox.checkState()

    def get_width(self) -> int:
        return self.checkBox.width()

    def set_position(self, position: list) -> None:
        position = [position[0] - self.get_width() // 2, position[1]]
        self.checkBox.move(position[0], position[1])

    def set_state(self, state=False):
        self.checkBox.setCheckState(state)

    def set_state_box(self):
        self.checkBox.setCheckState(1)

    def set_state_check(self):
        self.checkBox.setCheckState(2)