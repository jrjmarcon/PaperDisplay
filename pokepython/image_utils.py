from PIL import Image, ImageDraw, ImageFont

def draw_time_image(time_str, size=(250, 122), font_path=None, font_size=24):
    """
    Creates a PIL image with the current time centered.
    
    Args:
        time_str (str): Time string to display, e.g., "14:35"
        size (tuple): Width and height of the image
        font_path (str): Optional path to a TTF font file
        font_size (int): Font size for the time string

    Returns:
        PIL.Image.Image: Rendered image
    """
    w, h = size
    image = Image.new('1', (w, h), 255)  # White background
    draw = ImageDraw.Draw(image)

    # Use default font or load custom one
    if font_path:
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception:
            font = ImageFont.load_default()
    else:
        font = ImageFont.load_default()

    # Calculate text size and center position
    bbox = draw.textbbox((0, 0), time_str, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    x = (w - text_w) // 2
    y = (h - text_h) // 2

    draw.text((x, y), time_str, font=font, fill=0)  # Black text

    return image