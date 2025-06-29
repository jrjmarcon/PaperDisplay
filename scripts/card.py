from time import sleep
from datetime import datetime

from pokepython.models.pokemon_card import PokemonCard #import the PokemonCard Class
from services.pokemon_api import get_card_info #import the service function

from drivers import epd2in13_V4
from pokepython.display import Display


def main():
    epd = epd2in13_V4.EPD()

    print("Initializing e-paper display...")
    epd.init()
    epd.Clear()

    display = Display(epd)

    try:
        card_info = get_card_info("sv10-232")
        if card_info is None:
            print("Failed to fetch time from API, retrying in 10 seconds")
            return

        price_str = f"${card_info.price:.2f}"

        print(f"Displaying price: {card_info.price}")

        display.show_time(price_str)


    except KeyboardInterrupt:
        print("Interrupted. Putting display to sleep...")
        epd.Clear(0xFF)  # 0xFF = white, 0x00 = black
        epd.sleep()


if __name__ == "__main__":
    main()