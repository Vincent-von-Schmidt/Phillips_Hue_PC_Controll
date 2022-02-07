from PyQt5.QtWidgets import QPushButton


class Button:
    def __init__(
            self,
            widget: object,
            text: str,
            position: list = None,
            on_click = None,
            tool_tip: str = None,
            style_identifier: str = None
    ):
        self.widget = widget
        self.text = text
        self.tool_tip = tool_tip

        # create the button object
        self.button = QPushButton(self.text, self.widget)

        # define the position of the button
        if position is not None:
            self.set_position(position)

        # add a tooltip to the button
        if self.tool_tip is not None:
            self.set_tool_tip(self.tool_tip)

        # set on_click_action
        if on_click is not None:
            self.connect(on_click)

        if style_identifier is not None:
            self.button.setObjectName(style_identifier)

    def set_tool_tip(self, text: str) -> None:
        self.button.setToolTip(text)

    def set_position(self, position: list) -> None:
        position = [position[0] - self.get_width() // 2, position[1]]
        self.button.move(position[0], position[1])

    def get_width(self) -> int:
        return self.button.width()

    def get_height(self) -> int:
        return self.button.height()

    def connect(self, function):
        self.button.clicked.connect(function)



