import pytest

def test_is_scratch3_blank(parser):
    result = parser.is_scratch3(dict())
    assert result == False

def test_is_scratch3_incomplete(parser):
    result = parser.is_scratch3({"targets": {1, 2, 3}})
    assert result == False

def test_is_scratch3_empty(parser, empty_sb3):
    result = parser.is_scratch3(empty_sb3)
    assert result == True

def test_is_scratch3_full(parser, full_sb3):
    result = parser.is_scratch3(full_sb3)
    assert result == True

def test_is_scratch3_sb2(parser, small_sb2):
    result = parser.is_scratch3(small_sb2)
    assert result == False
    