import pytest

def test_get_block_comments_nonexistent(parser):
    result = parser.get_block_comments(dict())
    assert result == False

def test_get_block_comments_empty(parser, empty_sb3):
    result = parser.get_block_comments(empty_sb3)
    assert type(result) == dict
    assert len(result) == 0

def test_get_block_comments_full(parser, full_sb3):
    result = parser.get_block_comments(full_sb3)
    assert type(result) == dict
    assert len(result) == 1
    assert result["event_whenflagclicked"] == ["Comment!"]