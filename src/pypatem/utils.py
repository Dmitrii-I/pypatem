"""Utilities."""


class WhiteSpaceStripper:
    """Class implementing functionality to strip white-space."""

    description: str = "This class provides functionality to strip white-space from both ends of a strings."

    def __init__(self, left: bool = True, right: bool = True):
        """Initialize an object of class `WhiteSpaceStripper`.

        Parameter `left` indicates whether to strip white-space on the left. Parameter `right` is for the right-hand
        side.
        """
        self.left = left
        self.right = right

    def stripped(self, text: str) -> str:
        """Return `text` stripped of white-spaces."""
        if self.left:
            text = text.lstrip()

        if self.right:
            text.rstrip()

        return text
