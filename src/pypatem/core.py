import sqlparse

from pypatem.utils import WhitespaceStripper


def sql_tokens(query: str) -> list:
    """Returns SQL tokens by parsing `query`."""
    query = WhitespaceStripper(left=True, right=True).stripped(text=query)
    tokens = sqlparse.parse(sql=query)
    return tokens
