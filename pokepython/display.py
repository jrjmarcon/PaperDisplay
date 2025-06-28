from pokepython.image_utils import draw_time_image

class Display:
    def __init__(self, epd):
        self.epd = epd
        self.width = epd.height  # Swap width/height if landscape
        self.height = epd.width

    def show_time(self, time_str):
        image = draw_time_image(
            time_str,
            size=(self.width, self.height),
            font_size=48  # Adjust for readability
        )
        self.epd.display(self.epd.getbuffer(image))