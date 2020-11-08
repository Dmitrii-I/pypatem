"""Tests of module `core`."""

from pypatem.core import sql_tokens


def test_sql_tokens() -> None:
    """Test `sql_tokens` function."""
    print(sql_tokens(query="select * from users"))
