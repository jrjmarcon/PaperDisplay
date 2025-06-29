import os #to access environment variables
import requests #for making requests to the API
from pokepython.models.pokemon_card import PokemonCard
from dotenv import load_dotenv #for loading variables from the .env file

load_dotenv() #load environment variables from .env file

API_KEY = os.getenv("POKE_KEY")
BASE_URL = "https://api.pokemontcg.io/v2"

HEADERS = {
    "X-Api-Key": API_KEY
}

if not API_KEY:
    raise ValueError("API key not found. Please check your .env file or environment variables")

def get_card_info(card_id):
    url = f"{BASE_URL}/cards/{card_id}"
    response = requests.get(url, headers=HEADERS)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch card data: {response.status_code}")


    data = response.json()["data"]

    name = data.get("name")
    set_name = data.get("set", {}).get("name")
    artist = data.get("artist")

    prices = data.get("tcgplayer", {}).get("prices", {})
    market_price = None

    for price_data in prices.values():
        market_price = price_data.get("market")
        if market_price is not None:
            break

    card = PokemonCard(name=name, set_name=set_name, artist=artist, price=market_price)
    return card


if __name__ == "__main__":
    card_id = "sv10-232"  # Example card ID
    try:
        card = get_card_info(card_id)
        print(card)
    except Exception as e:
        print(e)