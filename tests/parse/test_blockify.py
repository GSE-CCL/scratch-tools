import pytest

def test_blockify_noargs(parser):
    with pytest.raises(ValueError):
        parser.blockify()

def test_blockify_f_nonexistent(parser):
    result = parser.blockify(file_name="tests/fixtures/nonexistent.json")
    assert result == False

def test_blockify_f_empty(parser):
    result = parser.blockify(file_name="tests/fixtures/empty.json")
    assert type(result) == dict
    assert len(result) == 10

def test_blockify_f_full(parser):
    result = parser.blockify(file_name="tests/fixtures/full.json")
    assert type(result) == dict
    assert len(result) == 10

def test_blockify_d_nonexistent(parser):
    result = parser.blockify(scratch_data=dict())
    assert result == False

def test_blockify_d_empty(parser, empty_sb3):
    result = parser.blockify(scratch_data=empty_sb3)
    assert type(result) == dict
    assert len(result) == 10

def test_blockify_d_full(parser, full_sb3):
    result = parser.blockify(scratch_data=full_sb3)
    assert type(result) == dict
    assert len(result) == 10
