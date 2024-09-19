"""Test move_info file and functions within it"""
from poketeambuild.move_info import Move

# Lets test with pound! 
move = Move(name = "pound")
def test_whoami():
    assert move.whoami() == "pound"
    
def test_get_move_info():
    move.get_move_info()
    assert move.accuracy is not None and move.power is not None and move.pp is not None and move.type is not None