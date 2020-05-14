import pytest

def test_get_sprite_names_nodata(parser):
    result = parser.get_sprite_names(dict())
    assert result == False

def test_get_sprite(parser, full_sb3):
    result = parser.get_sprite_names(full_sb3)
    assert type(result) == list
    assert result == ["Scratch"]
