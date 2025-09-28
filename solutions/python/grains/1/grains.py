def square(number):
    """Calculate the number of grains on a given square of a chessboard.

    :param number: int - the square number (1 through 64).
    :return: int - number of grains on the square, following the rule
            that each square has twice as many grains as the previous one.

    Raises a ValueError if the number is not between 1 and 64.
    """
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Calculate the total number of grains on a 64-square chessboard.

    :return: int - total number of grains on all 64 squares,
            following the rule that each square has twice as many
            grains as the previous one.
    """
    grains = 0
    for index in range(1, 64 + 1):
        grains += square(index)
    return grains