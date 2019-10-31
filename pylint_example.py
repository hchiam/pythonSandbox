"""
To run python linter pylint on this file, run this in the CLI:
pylint pylint_example.py
"""

# pylint: disable=too-few-public-methods

# learn unit testing in python later: https://www.youtube.com/watch?v=6baJ5t83820

class Example:
    """
    example class docstring
    """
    def __init__(self, number):
        self.number = number

    def example_method(self, number):
        """example method docstring"""
        return self.number + number
