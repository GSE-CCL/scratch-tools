import pytest

def test_get_variables_nonexistent(parser):
    result = parser.get_variables(dict())
    assert result == False

def test_get_variables_empty(parser, empty_sb3):
    result = parser.get_variables(empty_sb3)
    assert type(result) == list
    assert len(result) == 0
    assert result == []

def test_get_variables_full(parser, full_sb3):
    result = parser.get_variables(full_sb3)
    assert type(result) == list
    assert len(result) == 1
    assert result == ["test_variable"]