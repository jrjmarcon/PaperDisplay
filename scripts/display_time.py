#!/usr/bin/env python3

from time import sleep
from datetime import datetime

from pokepython.models.clock_models import TimeData #import the TimeData Class
from services.clock_api import get_current_time #import the service function

from drivers import epd2in13_V4
from pokepython.display import Display


def main():
    epd = epd2in13_V4.EPD()

    print("Initializing e-paper display...")
    epd.init()
    epd.Clear()

    display = Display(epd)

    try:
        while True:
            current_time = get_current_time()
            if current_time is None:
                print("Failed to fetch time from API, retrying in 10 seconds")
                sleep(10)
                continue

            time_str = f"{current_time.hour:02d}:{current_time.minute:02d}"
            # Syntax explanation:
            # f"" tells python to interpret string as f-string allowing embedded expressions with {}
            # 02d is a format specifer

            print(f"Displaying time: {time_str}")
            display.show_time(time_str)

            # Wait until next minute
            now = datetime.utcnow()
            seconds_until_next_minute = 60 - now.second
            sleep(seconds_until_next_minute)

    except KeyboardInterrupt:
        print("Interrupted. Putting display to sleep...")
        epd.Clear(0xFF)  # 0xFF = white, 0x00 = black
        epd.sleep()


if __name__ == "__main__":
    main()