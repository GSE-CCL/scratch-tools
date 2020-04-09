import pytest

def test_get_categories_nonexistent(parser):
    result = parser.get_categories(dict())
    assert result == False

def test_get_categories_empty(parser, empty_sb3):
    result = parser.get_categories(empty_sb3)
    assert type(result) == dict
    assert len(result) == 9
    assert result == {
        "motion": 0,
        "control": 0,
        "event": 0,
        "looks": 0,
        "operators": 0,
        "sensing": 0,
        "sound": 0,
        "more_blocks": 0,
        "data": 0
    }

def test_get_categories_full(parser, full_sb3):
    result = parser.get_categories(full_sb3)
    assert type(result) == dict
    assert len(result) == 9
    assert result == {
        "motion": 2,
        "control": 3,
        "event": 3,
        "looks": 2,
        "operators": 2,
        "sensing": 2,
        "sound": 2,
        "more_blocks": 2,
        "data": 2
    }