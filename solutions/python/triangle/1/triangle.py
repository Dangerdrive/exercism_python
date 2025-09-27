def valid_triangle(sides):
    """
    Check whether three side lengths can form a valid triangle.

    A triangle is valid if all sides are greater than zero and the
    sum of the two smaller sides is greater than the largest side.

    Args:
        sides (list[int]): A list of three integers representing
            the side lengths.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.
    """
    a, b, c = sorted(sides)
    return a > 0 and a + b > c


def equilateral(sides):
    """
    Check whether the given sides form an equilateral triangle.

    An equilateral triangle has all three sides equal and must
    satisfy the triangle inequality.

    Args:
        sides (list[int]): A list of three integers representing
            the side lengths.

    Returns:
        bool: True if the sides form an equilateral triangle,
        False otherwise.
    """
    return len(set(sides)) == 1 and valid_triangle(sides)


def isosceles(sides):
    """
    Check whether the given sides form an isosceles triangle.

    An isosceles triangle has at least two equal sides and must
    satisfy the triangle inequality.

    Args:
        sides (list[int]): A list of three integers representing
            the side lengths.

    Returns:
        bool: True if the sides form an isosceles triangle,
        False otherwise.
    """
    if 0 in sides:
        return False
    return len(set(sides)) <= 2 and valid_triangle(sides)


def scalene(sides):
    """
    Check whether the given sides form a scalene triangle.

    A scalene triangle has all sides of different lengths and
    must satisfy the triangle inequality.

    Args:
        sides (list[int]): A list of three integers representing
            the side lengths.

    Returns:
        bool: True if the sides form a scalene triangle,
        False otherwise.
    """
    if 0 in sides:
        return False
    return len(set(sides)) == 3 and valid_triangle(sides)