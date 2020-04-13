import pytest

def test_get_child_blocks_nodata(parser):
    result = parser.get_child_blocks("fakeid", dict())
    assert result == False

def test_get_child_blocks_nonexistent(parser, full_sb3):
    result = parser.get_child_blocks("fakeid", full_sb3)
    assert result == ["fakeid"]

def test_get_child_blocks_substack(parser, full_sb3):
    result = parser.get_child_blocks("CupN)`F`z1tugXtDqYzj", full_sb3)
    assert type(result) == list
    assert result == ["CupN)`F`z1tugXtDqYzj", "G+C7yL/-O.6MH2V,f@DG", "(Psor|t+4_@pna[eo4{0", "Fw-*+6_[m%^1H#z%J9:5", "Zb.aqYN8g)eq3U?(dp8D", "AY_Zzu5][G2PdI|k6U0=", "8ehy)TEZADt*EPqfDy3("]
    
def test_get_child_blocks_event_listener(parser, full_sb3):
    result = parser.get_child_blocks("/T~TiqeE4Xip(IQA6gZz", full_sb3)
    assert type(result) == list
    assert result == ["/T~TiqeE4Xip(IQA6gZz", "0.OsCi6`8oaNdL~)e{=.", "=;8*+!W%HjdlwP5oUcHd"]
