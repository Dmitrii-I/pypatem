"""Module containing core functionality of the package."""

from typing import List

import sqlparse

from pypatem.utils import WhitespaceStripper


def sql_tokens(query: str) -> List[sqlparse.tokens.Token]:
    """Return SQL tokens by parsing `query`."""
    query = WhitespaceStripper(left=True, right=True).stripped(text=query)
    tokens = sqlparse.parse(sql=query)
    return tokens
