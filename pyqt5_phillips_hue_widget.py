from widgets import widgetButton, widgetLabel, widgetSlider
import functions
import format
import p_hue


class PhillipsHuePanel:
    def __init__(
            self,
            widget: object,
            position: list,
            light: int,
            hue_ip: str,
            hue_user: str,
            name: str = None
    ):

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

            self.hue_slider.connect(
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
            on_click=lambda: functions.combineFunctions(
                self.light.set_state(data={"on": True}),
                self.set_current_state()
            )
        )
        self.objects.append(self.on_button)

        self.off_button = widgetButton.Button(
            widget=self.widget,
            text="off",
            on_click=lambda: self.light.set_state(data={"on": False})
        )
        self.objects.append(self.off_button)

        # set position
        self.set_position(position)

    def set_position(self, position: list) -> None:
        height = []
        width = (self.bri_text.get_width() + self.bri_slider.get_width() + 74) // 2
        gap_height = 15

        self.objects.pop(0)
        # self.objects.pop(len(self.objects) - 1)

        var = 0
        for index, content in enumerate(self.objects[:len(self.objects) // 2:]):
            var += content.get_height()
            var += gap_height
            height.insert(index, var)

        for index, content in enumerate(height[::-1]):
            height.insert(index, -content)

        for i in range(2):
            height.pop(0)
        height.pop(len(height) - 1)

        height.insert(len(height) // 2, 0)

        self.headline.set_position([position[0] + width // 12, position[1] + height[0]])
        self.on_button.set_position([position[0] - width // 3, position[1] + height[len(height) - 1]])
        self.off_button.set_position([position[0] + width // 3, position[1] + height[len(height) - 1]])

        # set the position from the texts
        for index, content in enumerate(self.objects[::2]):
            content.set_position([position[0] - width // 3, position[1] + height[index] + 50])

        # set the position from the sliders
        for index, content in enumerate(self.objects[1::2]):
            content.set_position([position[0] + width // 3, position[1] + height[index] + 50])

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
