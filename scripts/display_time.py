#!/usr/bin/env python3

from time import sleep
from datetime import datetime

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
            now = datetime.now()
            time_str = now.strftime('%H:%M')

            print(f"Displaying time: {time_str}")
            display.show_time(time_str)

            # Wait until next minute
            seconds_until_next_minute = 60 - now.second
            sleep(seconds_until_next_minute)

    except KeyboardInterrupt:
        print("Interrupted. Putting display to sleep...")
        epd.sleep()


if __name__ == "__main__":
    main()