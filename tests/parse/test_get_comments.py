import pytest

def test_get_comments_nonexistent(parser):
    result = parser.get_comments(dict())
    assert result == False

def test_get_comments_empty(parser, empty_sb3):
    result = parser.get_comments(empty_sb3)
    assert type(result) == list
    assert len(result) == 0

def test_get_comments_full(parser, full_sb3):
    result = parser.get_comments(full_sb3)
    assert type(result) == list
    assert len(result) == 1
    assert result == ["Comment!"]