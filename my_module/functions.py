"""A collection of function for doing my project."""

def instructions():
    """Provides instructions on how to play the game to the player"""
    
    print("Friday The 13th: Escape" +
          "\n-------------------------------------" +
          "\nControls:" +
          "\ngo [direction]" +
          "\ndirections: up, down, left, right"
          "\n-------------------------------------")


def show_location(present_location):
    """Constantly shows the current location of the player in the game"""
    
    new_location = present_location
    
    print("Player location: " + new_location)
    
    return new_location