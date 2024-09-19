"""Code to find a pokemon and give all it's attributes, abilities etc"""

import requests

class Pokemon():
    def __init__(self, name = str) -> None:
        # On initialisation the user will give a pokemon name which we then use to get all the info
        self.name = name.lower()
        self.stats, self.types, self.moves = self.get_pokemon_info()
    
    def whoami(self):
        return self.name
    
    # We want to only run this in the init when the pokemon is first selected by the player
    def get_pokemon_info(self):
        try:
            r = requests.get(f'https://pokeapi.co/api/v2/pokemon/{self.name}')
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            # The only error handling that we want to do is if there is a misspelling 
            # Change this to be something different but that will need to reply on upstream
            return None, None, None
        
        info = r.json()
        moves = [i["move"] for i in info['moves']]
        
        return info['stats'], info['types'], moves