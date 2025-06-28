from datetime import datetime
import time

from pokepython.image_utils import draw_time_image
from pokepython.display import show_image_on_epaper

def main():
    try:
        while True:
            now = datetime.now()
            time_str = now.strftime("%H:%M")

            imgage = draw_time_image(time_str)

            show_image_on_epaper(image)

            seconds_to_wait = 60 - now.second

            time.sleep(seconds_to_wait)
    except KeyboardInterrupt:
        print("Simulation stopped.")
    
if __name__ == "__main__":
    main()