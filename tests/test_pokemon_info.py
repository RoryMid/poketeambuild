"""Test pokemon_info file and functions within it"""
from poketeambuild.pokemon_info import Pokemon

# Lets test with Haunter!
haunter = Pokemon(name = "Haunter")
def test_get_name():
    assert haunter.get_name() == "Haunter"