from dataclasses import dataclass

@dataclass
class PokemonCard:
    name: str
    set_name: str
    artist: str
    price: float