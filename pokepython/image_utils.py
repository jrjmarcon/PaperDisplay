from PIL import Image, ImageDraw, ImageFont
import warnings

def draw_time_image(time_str, size=(250, 122), font_path=None, font_size=48):
    """
    Creates a PIL image with the time string centered.
    """
    w, h = size
    image = Image.new('1', (w, h), 255)  # 1-bit image, white background
    draw = ImageDraw.Draw(image)

    # Load font
    if font_path:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception as e:
            warnings.warn(f"Failed to load font from {font_path}: {e}")
            font = ImageFont.load_default()
    else:
        try:
            font = ImageFont.truetype(
                "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
                font_size
            )
        except Exception:
            font = ImageFont.load_default()

    # Calculate text position to center it
    bbox = draw.textbbox((0, 0), time_str, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (w - text_w) // 2
    y = (h - text_h) // 2

    draw.text((x, y), time_str, font=font, fill=0)  # Black text

    return image