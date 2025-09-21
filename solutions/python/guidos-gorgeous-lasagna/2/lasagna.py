"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

EXPECTED_BAKE_TIME: int  = 40
PREPARATION_TIME: int = 2

#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(elapsed_bake_time: int) -> int: 
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    
    

def preparation_time_in_minutes(number_of_layers: int) -> int:
    """Calculate the preparation time.

    :param number_of_layers: int - how many lawyers the lasagna has.
    :return: int - how much time the lasagna preparation (in minutes) derived from 'number of layers'.

    Function that takes the number of layers the lasagna has 
    and returns how many minutes the lasagna will take to be prepared.
    """
    return number_of_layers * PREPARATION_TIME
    

def elapsed_time_in_minutes(number_of_layers: int, elapsed_bake_time: int) -> int:
    """Calculate the elapsed time.

    :param number_of_layers: int - how many lawyers the lasagna has.
    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - how much time (in minutes) elapsed.

    Function that takes the number of layers the lasagna has and bake time elapsed
    and returns how many minutes elapsed in total.
    """
    return EXPECTED_BAKE_TIME - bake_time_remaining(elapsed_bake_time) + preparation_time_in_minutes(number_of_layers)

