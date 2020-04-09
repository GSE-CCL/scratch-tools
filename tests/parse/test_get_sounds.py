import pytest

def test_get_sounds_nonexistent(parser):
    result = parser.get_sounds(dict())
    assert result == False

def test_get_sounds_empty(parser, empty_sb3):
    result = parser.get_sounds(empty_sb3)
    assert type(result) == list
    assert len(result) == 0

def test_get_sounds_full(parser, full_sb3):
    result = parser.get_sounds(full_sb3)
    assert type(result) == list
    assert len(result) == 2
    assert result == ["pop", "Sound!"]