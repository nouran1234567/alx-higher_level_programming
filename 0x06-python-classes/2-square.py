#!/usr/bin/python3
"""Square module."""

# class Square that defines a square


class Square:
    """Defines a square class."""

    def __init__(self, size=0):
        """Initialize a Square.
        Args:
            size (int): Size length of new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
