import epd2in13_V4
import time
from PIL import Image, ImageDraw, ImageFont

def main():
    epd = epd2in13_V4.EPD()
    epd.init() # wakes the screen

    w = epd.width
    h = epd.height

    font = ImageFont.load_default()         #load a basic font for drawing the text

    # Wipe with white
    image = Image.new('1', (w,h),255)       # create a white image
    draw = ImageDraw.Draw(image)            #create a drawing context to draw on the image
    draw.text((10, 50), "Hello, world!", font=font, fill=0) # draw black text on the white screen
    buffer = epd.getbuffer(image)           # convert to raw display format that ePaper display understands
    epd.display(buffer)                     # send to screen to show it
    time.sleep(2)                           # pauses execution for 2 seconds so display has time to update

    # Then black
    image = Image.new('1', (w,h),0)         # black image
    draw = ImageDraw.Draw(image)
    draw.text((10, 50), "Hello, world! (now in black!)", font=font, fill=255) # draw white text on the black screen
    buffer = epd.getbuffer(image)           # convert to raw display format
    epd.display(buffer)                     # send to screen
    time.sleep(2)                           # pauses execution for 1 second

    # Wipe with white again
    image = Image.new('1', (w,h),255)       # create a white image
    buffer = epd.getbuffer(image)           # convert to raw display format that ePaper display understands
    epd.display(buffer)                     # send to screen to show it
    time.sleep(2) 

    epd.sleep()                             # tells controller to shut down

if __name__ == '__main__':
    main()