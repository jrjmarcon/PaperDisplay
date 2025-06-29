import requests

API_KEY = "key-here" 
BASE_URL = "https://api.pokemontcg.io/v2"
HEADERS = {"X-Api-Key": API_KEY}

def get_card_id_by_name_and_set(card_name, set_name):
    # Build the query string
    query = f'name:"{card_name}" set.name:"{set_name}"'
    url = f"{BASE_URL}/cards"
    params = {"q": query}

    # Make the API request
    response = requests.get(url, headers=HEADERS, params=params)
    response.raise_for_status()
    
    # Parse the response
    cards = response.json().get("data", [])
    if not cards:
        print(f"No cards found for '{card_name}' in set '{set_name}'")
        return None

    # Print results
    ids = []
    for card in cards:
        card_id = card['id']
        ids.append(card_id)
        print(f"ID: {card_id} | Name: {card['name']} | Set: {card['set']['name']} | Number: {card['number']}")

    return ids if len(ids) > 1 else ids[0]  # Return single ID if only one match

# Replace with your API key and run:
result = get_card_id_by_name_and_set("Cynthia's Garchomp ex","Destined Rivals")
print(result)