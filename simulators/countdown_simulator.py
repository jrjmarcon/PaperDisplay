from PIL import Image, ImageDraw, ImageFont
import time

def center_text(draw, text, font, image_size):
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (image_size[0] - text_w) // 2
    y = (image_size[1] - text_h) // 2
    return x, y

def main():
    # Simulated display size in landscape (Waveshare 2.13" is 250x122)
    w, h = 250, 122
    landscape_size = (w, h)
    font = ImageFont.load_default()

    for i in range(5, 0, -1):
        image = Image.new('1', landscape_size, 255)  # white background
        draw = ImageDraw.Draw(image)

        text = str(i)
        pos = center_text(draw, text, font, landscape_size)
        draw.text(pos, text, font=font, fill=0)  # black text

        image.show()
        time.sleep(1)

    # Final white screen
    image = Image.new('1', landscape_size, 255)
    image.show()
    time.sleep(1)

if __name__ == '__main__':
    main()