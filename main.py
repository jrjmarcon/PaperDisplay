import epd2in13_V4
import time
from PIL import Image

def main():
    epd = epd2in13_V4.EPD()
    epd.init()

    w = epd.width
    h = epd.height

    # Wipe with white
    epd.display(epd.getbuffer(Image.new('1', (w, h), 255)))
    time.sleep(1)

    # Then black
    epd.display(epd.getbuffer(Image.new('1', (w, h), 0)))
    time.sleep(1)

    # Then white again
    epd.display(epd.getbuffer(Image.new('1', (w, h), 255)))
    time.sleep(2)

    epd.sleep()

if __name__ == '__main__':
    main()