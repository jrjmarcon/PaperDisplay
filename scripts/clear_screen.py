#!/usr/bin/env python3

from drivers import epd2in13_V4


def main():
    epd = epd2in13_V4.EPD()

    print("Initializing e-paper display...")
    epd.init()

    print("Clearing display to white...")
    epd.Clear(0xFF)  # 0xFF = white, 0x00 = black

    print("Putting display to sleep...")
    epd.sleep()

    print("Done. Display is cleared.")


if __name__ == "__main__":
    main()