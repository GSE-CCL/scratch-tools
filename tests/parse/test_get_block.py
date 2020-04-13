import pytest

def test_get_block_nodata(parser):
    result = parser.get_block("fakeid", dict())
    assert result == False

def test_get_block_nonexistent(parser, full_sb3):
    result = parser.get_block("fakeid", full_sb3)
    assert result == False

def test_get_block(parser, full_sb3):
    result = parser.get_block("CupN)`F`z1tugXtDqYzj", full_sb3)
    assert type(result) == dict
    assert result == {"opcode":"control_repeat", "next": None, "parent":"[f|hsFZ%vg~}7{C}=*%5", "inputs": {"TIMES": [1, [6, "10"]], "SUBSTACK":[2, "G+C7yL/-O.6MH2V,f@DG"]}, "fields":{}, "shadow":False, "topLevel":False}
