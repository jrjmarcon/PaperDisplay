from PIL import Image, ImageDraw, ImageFont
import time
from datetime import datetime

def draw_time_image(time_str, size=(250,122)):
    
    w,h = size
    image = Image.new('1', (w,h), 255)
    draw = ImageDraw.Draw(image)

    font = ImageFont.load_default()

    bbox = draw.textbbox((0,0), time_str, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    x = (w - text_w) // 2
    y = (h - text_h) // 2

    draw.text((x,y), time_str, font=font, fill=0)
    
    return image

def main():
    try:
        while True:
            now = datetime.now()
            time_str = now.strftime("%H:%M")

            img = draw_time_image(time_str)

            img.show()

            seconds_to_wait = 60 - now.second

            time.sleep(seconds_to_wait)
    except KeyboardInterrupt:
        print("Simulation stopped.")
    
if __name__ == "__main__":
    main()

# test commit