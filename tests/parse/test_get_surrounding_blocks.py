import pytest

def test_get_surrounding_blocks_nonexistent(parser):
    result = parser.get_surrounding_blocks("fakeid", dict())
    assert result == False

def test_get_surrounding_blocks_delve(parser, full_sb3):
    result = parser.get_surrounding_blocks("CupN)`F`z1tugXtDqYzj", full_sb3, delve=True)
    assert type(result) == list
    assert result == ["CupN)`F`z1tugXtDqYzj", "G+C7yL/-O.6MH2V,f@DG", "(Psor|t+4_@pna[eo4{0", "Fw-*+6_[m%^1H#z%J9:5", "Zb.aqYN8g)eq3U?(dp8D"]
    
def test_get_surrounding_blocks_even_count(parser, full_sb3):
    result = parser.get_surrounding_blocks("G+C7yL/-O.6MH2V,f@DG", full_sb3, count=4)
    assert type(result) == list
    assert result == ["CupN)`F`z1tugXtDqYzj", "G+C7yL/-O.6MH2V,f@DG", "(Psor|t+4_@pna[eo4{0", "Fw-*+6_[m%^1H#z%J9:5"]

def test_get_surrounding_blocks_no_delve(parser, full_sb3):
    result = parser.get_surrounding_blocks("CupN)`F`z1tugXtDqYzj", full_sb3)
    assert type(result) == list
    assert result == ["Aui.NpK5Cs_obawNI4{c", "[f|hsFZ%vg~}7{C}=*%5", "CupN)`F`z1tugXtDqYzj", "G+C7yL/-O.6MH2V,f@DG", "(Psor|t+4_@pna[eo4{0"]
