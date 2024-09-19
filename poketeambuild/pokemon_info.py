"""Code to find a pokemon and give all it's attributes, abilities etc"""

class Pokemon():
    def __init__(self, name = str) -> None:
        # On initialisation the user will give a pokemon name which we then use to get all the info
        self.name = name
    
    def get_name(self):
        return self.name
        