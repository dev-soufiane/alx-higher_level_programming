#!/usr/bin/python3
"""
Defines the MyInt class, a subclass of int with inverted equality operators.
"""


class MyInt(int):
    """Invert int operators == and !="""

    def __eq__(self, value):
        """
        Override == operator with != behavior.

        Args:
            value: The value to compare.

        Returns:
            bool: True if the real part is not equal to the value,
            False otherwise.
        """
        return self.real != value

    def __ne__(self, value):
        """
        Override != operator with == behavior.

        Args:
            value: The value to compare.

        Returns:
            bool: True if the real part is equal to the value, False otherwise.
        """
        return self.real == value
