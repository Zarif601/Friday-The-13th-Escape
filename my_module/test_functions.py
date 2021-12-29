"""Test for my functions."""

from functions import *


# Test for instructions
def test_instructions():

    assert instructions() == None
    
test_instructions()


location = { 'Cabin': {
                    'right' : 'Park walls',
                    'left'  : 'Where the dead body was found',
                    'up'    : 'Campfire'
}
               }
    
player_location = location['Cabin']['right']


# Test for show_location    
def test_show_location(player_location):
       
    assert show_location(player_location) == 'Park walls'

test_show_location(player_location)