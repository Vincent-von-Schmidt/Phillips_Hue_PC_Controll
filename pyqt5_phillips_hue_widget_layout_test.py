from widgets import widgetButton, widgetLabel, widgetSlider
from PyQt5.QtWidgets import QFormLayout, QWidget
import functions
import format
import p_hue


class PhillipsHuePanel(QWidget):
    def __init__(
            self,
            widget: object,
            position: list,
            light: int,
            hue_ip: str,
            hue_user: str,
            name: str = None
    ):
        super().__init__()

        self.layout = QFormLayout()
        self.widget = widget
        self.hue_ip = hue_ip
        self.hue_user = hue_user
        self.objects = []
        self.light = p_hue.PHueLight(self.hue_ip, self.hue_user, light)
        self.light_capabilities = self.light.get_capabilities()

        if name is not None:
            self.name = name
        else:
            self.name = self.light.get_name()

        self.headline = widgetLabel.Text(
            widget=self.widget,
            text=self.name,
            font_size=format.header_font_size,
            bold=True,
            style_identifier="headline"
        )
        self.objects.append(self.headline)

        self.bri_text = widgetLabel.Text(
            widget=self.widget,
            text="brightness",
            font_size=format.normal_font_size
        )
        self.objects.append(self.bri_text)

        self.bri_slider = widgetSlider.Slider(
            widget=self.widget,
            orientation="horizontal",
            on_change=lambda: self.light.set_state(
                data={
                    "on": True,
                    "bri": self.bri_slider.get_value()
                }
            ),
            start=0,
            stop=254,
            state_identifier="bri"
        )
        self.objects.append(self.bri_slider)

        # check if the light is capable to display color
        if self.light_capabilities["color"]:

            self.sat_text = widgetLabel.Text(
                widget=self.widget,
                text="saturation",
                font_size=format.normal_font_size
            )
            self.objects.append(self.sat_text)

            self.sat_slider = widgetSlider.Slider(
                widget=self.widget,
                orientation="horizontal",
                start=0,
                stop=254,
                state_identifier="sat"
            )
            self.objects.append(self.sat_slider)

            self.hue_text = widgetLabel.Text(
                widget=self.widget,
                text="color",
                font_size=format.normal_font_size
            )
            self.objects.append(self.hue_text)

            self.hue_slider = widgetSlider.Slider(
                widget=self.widget,
                orientation="horizontal",
                start=0,
                stop=50000,
                state_identifier="hue"
            )
            self.objects.append(self.hue_slider)

            self.sat_slider.connect(
                function=lambda: self.light.set_state(
                    data={
                        "on": True,
                        "bri": self.bri_slider.get_value(),
                        "sat": self.sat_slider.get_value(),
                        "hue": self.hue_slider.get_value(),
                        "colormode": "xy"
                    }
                )
            )

            # idea: color preview as background
            self.hue_slider.connect(
                function=lambda: functions.combine_functions(
                    self.light.set_state(
                        data={
                            "on": True,
                            "bri": self.bri_slider.get_value(),
                            "sat": self.sat_slider.get_value(),
                            "hue": self.hue_slider.get_value(),
                            "colormode": "xy"
                        }
                    )
                )
            )

        if self.light_capabilities["ct"]:

            self.ct_text = widgetLabel.Text(
                widget=self.widget,
                text="white",
                font_size=format.normal_font_size
            )
            self.objects.append(self.ct_text)

            self.ct_slider = widgetSlider.Slider(
                widget=self.widget,
                orientation="horizontal",
                on_change=lambda: self.light.set_state(
                    data={
                        "on": True,
                        "bri": self.bri_slider.get_value(),
                        "ct": self.ct_slider.get_value(),
                        "colormode": "ct"
                    }
                ),
                start=int(self.light.get_info()["capabilities"]["control"]["ct"]["min"]),
                stop=int(self.light.get_info()["capabilities"]["control"]["ct"]["max"]),
                state_identifier="ct"
            )
            self.objects.append(self.ct_slider)

        self.on_button = widgetButton.Button(
            widget=self.widget,
            text="on",
            style_identifier="on_button"
        )
        self.objects.append(self.on_button)

        self.off_button = widgetButton.Button(
            widget=self.widget,
            text="off",
            style_identifier="off_button"
        )
        self.objects.append(self.off_button)

        self.on_button.connect(lambda: functions.combine_functions(
            self.light.set_state(data={"on": True}),
            self.set_current_state(),
            self.on_button.set_style_identifier("on_button_activated"),
            self.off_button.set_style_identifier("off_button")
        ))

        self.off_button.connect(lambda: functions.combine_functions(
            self.light.set_state(data={"on": False}),
            self.on_button.set_style_identifier("on_button"),
            self.off_button.set_style_identifier("off_button_activated")
        ))

        # set position
        self.set_position(position)

    def set_position(self, position: list) -> None:
        self.layout.addRow(self.objects[0])

        for odd_content, even_content in zip(
                enumerate(self.objects[1::2]),
                enumerate(self.objects[2::2])
        ):
            self.layout.addRow(odd_content, even_content)

        self.setLayout(self.layout)

    def set_current_state(self) -> None:
        request = self.light.get_state()
        for content in self.objects:
            if isinstance(content, widgetSlider.Slider):
                if request["on"]:
                    if request["colormode"] == "ct":
                        if not content.state_identifier == "hue":
                            content.set_slider_to_number(
                                int(request[content.state_identifier])
                            )

                    elif request["colormode"] == "hue":
                        if not content.state_identifier == "ct":
                            content.set_slider_to_number(
                                int(request[content.state_identifier])
                            )
                    else:
                        content.set_slider_to_number(
                            int(request[content.state_identifier])
                        )

