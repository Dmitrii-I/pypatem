"""Utilities."""


class WhitespaceStripper:
    """Class implementing functionality to strip whitespace."""

    description: str = "This class provides functionality to strip whitespace from both ends of a strings."

    def __init__(self, left: bool = True, right: bool = True):
        """Initialize an object of class `WhitespaceStripper`.

        Parameter `left` indicates whether to strip whitespace on the left. Parameter `right` is for the right-hand
        side.
        """
        self.left = left
        self.right = right

    def stripped(self, text: str) -> str:
        """Return `text` stripped of whitespaces."""
        if self.left:
            text = text.lstrip()

        if self.right:
            text.rstrip()

        return text
