import pytest

def test_get_costumes_nonexistent(parser):
    result = parser.get_costumes(dict())
    assert result == False

def test_get_costumes_empty(parser, empty_sb3):
    result = parser.get_costumes(empty_sb3)
    assert type(result) == list
    assert len(result) == 1

def test_get_costumes_full(parser, full_sb3):
    result = parser.get_costumes(full_sb3)
    assert type(result) == list
    assert len(result) == 4
    assert result == ["backdrop1", "Bedroom 1", "cat1", "cat2"]