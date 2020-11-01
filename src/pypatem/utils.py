"""Utilities."""


class WhitespaceStripper:
    description: str = "This class provides functionality to strip whitespace from both ends of a strings."

    def __init__(self, left: bool = True, right: bool = True):
        self.left = left
        self.right = right

    def stripped(self, text: str) -> str:

        if self.left:
            text = text.lstrip()

        if self.right:
            text.rstrip()

        return text
