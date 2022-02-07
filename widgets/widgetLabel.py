from PyQt5.QtWidgets import QLabel


class Text:
    def __init__(
            self,
            widget: object,
            text: str,
            font_size: int,
            position: list = None,
            bold: bool = False,
            color: str = 'black',
            tool_tip: str = None,
            style_identifier: str = None
    ):
        self.widget = widget
        self.text = text
        self.bold = bold
        self.color = color
        self.tool_tip = tool_tip

        # add px to the fontSize var
        self.font_size = '{}px'.format(font_size)

        # check if the fontWeight are bold or normal and send this to the style
        if self.bold:
            self.font_weight = 'bold'
        else:
            self.font_weight = 'normal'

        self.label = QLabel(self.widget)

        # set the text and the style
        self.set_text(self.text)

        # add a tooltip
        if self.tool_tip is not None:
            self.label.setToolTip(self.tool_tip)

        # set position
        if position is not None:
            self.set_position(position)

        if style_identifier is not None:
            self.label.setObjectName(style_identifier)

    def set_text(self, text):
        self.label.setText(text)

    def set_position(self, position: list) -> None:
        position = [position[0] - self.get_width() // 2, position[1]]
        self.label.move(position[0], position[1])

    def get_width(self) -> int:
        return self.label.width()

    def get_height(self) -> int:
        return self.label.height()

