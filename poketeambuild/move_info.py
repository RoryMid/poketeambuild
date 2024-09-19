"""Code to find a pokemon and give all it's attributes, abilities etc"""

import requests

class Move():
    def __init__(self, name = str) -> None:
        # On initialisation the user will give a pokemon name which we then use to get all the info
        self.name = name
        self.accuracy, self.power, self.pp, self.type = self.get_move_info()
    
    def whoami(self):
        return self.name
        
    def get_move_info(self):
        r = requests.get(f"https://pokeapi.co/api/v2/move/{self.name}")
        r.raise_for_status() # Should only get moves from the api so no error handling allowing it to raise
        
        info =  r.json()
        
        return info['accuracy'], info['power'], info['pp'], info['type']