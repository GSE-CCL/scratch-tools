import pytest

def test_blockify_nonexistent(parser):
    result = parser.blockify("fixtures/nonexistent.json")
    assert result == False

def test_blockify_empty(parser):
    result = parser.blockify("fixtures/empty.json")
    assert type(result) == dict
    assert len(result) == 7

def test_blockify_full(parser):
    result = parser.blockify("fixtures/full.json")
    assert type(result) == dict
    assert len(result) == 7