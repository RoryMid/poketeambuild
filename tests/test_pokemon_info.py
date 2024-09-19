"""Test pokemon_info file and functions within it"""
from poketeambuild.pokemon_info import Pokemon
import pytest, requests

# Lets test with Haunter! Add the odd capital etc
haunter = Pokemon(name = "HaUnter")
def test_whoami():
    assert haunter.whoami() == "haunter"
    
def test_get_pokemon_info():
    haunter.get_pokemon_info()
    assert haunter.moves is not None and haunter.stats is not None and haunter.types is not None
    
hanter = Pokemon(name = "hanter")
def test_bad_get_pokemon_info():
    hanter.get_pokemon_info()
    assert hanter.moves is None and hanter.stats is None and hanter.types is None