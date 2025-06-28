from drivers import EPD
import time

# Initialize and configure the display
def initialize_display():
    epd = EPD()
    epd.init()
    epd.Clear()
    return epd

# Send a PIL image to the e-paper display
def show_image_on_epaper(image, rotate=True):
    epd = EPD()
    epd.init()

    if rotate:
        image = image.rotate(90, expand=True)

    buffer = epd.getbuffer(image)
    epd.display(buffer)

    time.sleep(2)  # Give the display time to refresh

    epd.sleep()