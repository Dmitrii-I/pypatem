"""Module containing core functionality of the package."""

from typing import List

import sqlparse

from pypatem.utils import WhiteSpaceStripper


def sql_tokens(query: str) -> List[str]:
    """Return SQL tokens by parsing `query`."""
    query = WhiteSpaceStripper(left=True, right=True).stripped(text=query)
    tokens = [str(token) for token in sqlparse.parse(sql=query)]
    return tokens
