from PIL import Image, ImageDraw, ImageFont
import time

def create_display_image(bg_color, text, text_color):
    w, h = 250, 122  # Approx size for 2.13" display; adjust as needed
    image = Image.new('1', (w, h), bg_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 50), text, font=font, fill=text_color)
    return image

def main():
    # Simulate white screen with black text
    image1 = create_display_image(255, "Hello, world!", 0)
    image1.show()
    time.sleep(2)

    # Simulate black screen with white text
    image2 = create_display_image(0, "Hello, world! (now in black!)", 255)
    image2.show()
    time.sleep(2)

    # Simulate wiping with white again
    image3 = Image.new('1', (250, 122), 255)
    image3.show()
    time.sleep(2)

if __name__ == '__main__':
    main()