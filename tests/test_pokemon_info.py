"""Test pokemon_info file and functions within it"""
from poketeambuild.pokemon_info import Pokemon

# Lets test with Haunter! Add the odd capital etc
haunter = Pokemon(name = "HaUnter")
def test_whoami():
    assert haunter.whoami() == "haunter"
    
def test_get_pokemon_info():
    info = haunter.get_pokemon_info()
    assert info["name"] == "haunter"