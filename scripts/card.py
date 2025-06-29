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
    
    update_int = 1 # update interval in minutes

    while True:
        try:
            card_info = get_card_info("sv10-232")

            if card_info is None:
                print("[WARNING] Failed to fetch time from API, retrying in 10 seconds")
                sleep(10)
                continue # skips the rest of the loop and starts over
            
            price_str = f"${card_info.price:.2f}"
            
            print(f"[SUCCESS]Displaying updated price: {price_str}")
            display.show_time(price_str)

            print(f"[INFO] Sleeping for {update_int} minute(s)...\n")
            sleep(update_int * 60)

        except KeyboardInterrupt:
            print("\n[INFO] Interrupted. Putting display to sleep...")
            epd.Clear(0xFF)  # 0xFF = white, 0x00 = black
            epd.sleep()
            break

        except Exception as e:
            print(f"[ERROR] {e}. Retrying in 10 seconds...")
            sleep(10)


if __name__ == "__main__":
    main()