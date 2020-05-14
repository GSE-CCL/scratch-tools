import pytest

def test_get_block_text_nodata(parser):
    result = parser.get_block_text(dict())
    assert result == False

def test_get_block_text_empty(parser, empty_sb3):
    result = parser.get_block_text(empty_sb3)
    assert type(result) == list
    assert result == []

def test_get_block_text_empty(parser, user_text_sb3):
    result = parser.get_block_text(user_text_sb3)
    assert type(result) == list
    assert result == ["saying for a period", "just saying something", "thinking for a period", "just thinking something", "asking the user a question"]
