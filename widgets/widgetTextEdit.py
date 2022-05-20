from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt


class LineEdit:
    def __init__(
            self,
            widget,
            position: list = None,
            text_length: int = 0,
            length: int = 150,
            alignment: str = 'left',
            on_change=None,
            text: str = None,
            tool_tip: str = None,
            placeholder_text: str = None
    ):
        self.widget = widget
        self.tool_tip = tool_tip
        self.text = text
        self.length = length
        self.text_length = text_length
        self.placeholder_text = placeholder_text

        if alignment == 'left':
            self.alignment = Qt.AlignLeft
        elif alignment == 'center':
            self.alignment = Qt.AlignCenter
        elif alignment == 'right':
            self.alignment = Qt.AlignRight
        else:
            raise TypeError('LineEdit : alignment --> left, center, right')

        # create the object
        self.lineEdit = QLineEdit(self.widget)

        # define the position
        if position is not None:
            self.set_position(position)

        # set text
        self.lineEdit.setText(self.text)

        # set alignment
        self.lineEdit.setAlignment(self.alignment)

        # set length
        self.lineEdit.setFixedWidth(self.length)

        self.lineEdit.setPlaceholderText("Test")

        if self.placeholder_text is not None:
            self.lineEdit.setPlaceholderText(self.placeholder_text)

        # set max text length
        if not self.text_length == 0:
            self.lineEdit.setMaxLength(self.text_length)

        # define a tooltip
        if self.tool_tip is not None:
            self.set_tool_tip(self.tool_tip)

        # set on_change action
        if on_change is not None:
            self.connect(on_change)

    def set_position(self, position: list) -> None:
        position = [int(position[0] - self.get_width() // 2), int(position[1] - self.get_height() // 2)]
        self.lineEdit.move(position[0], position[1])

    def set_tool_tip(self, text: str) -> None:
        self.lineEdit.setToolTip(text)

    def get_width(self) -> int:
        return self.lineEdit.width()

    def get_height(self) -> int:
        return self.lineEdit.height()

    def get_user_input(self):
        return self.lineEdit.text()

    def connect(self, function):
        self.lineEdit.textChanged.connect(function)
