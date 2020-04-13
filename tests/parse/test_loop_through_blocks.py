import pytest

def test_loop_through_blocks_nonexistent(parser):
    result = parser.get_child_blocks("fakeid", dict())
    assert result == False

def test_loop_through_blocks_next(parser, full_sb3):
    result = parser.loop_through_blocks("0.OsCi6`8oaNdL~)e{=.", full_sb3, mode="next")
    assert type(result) == list
    assert result == ["0.OsCi6`8oaNdL~)e{=.", "=;8*+!W%HjdlwP5oUcHd"]

def test_loop_through_blocks_parent(parser, full_sb3):
    result = parser.loop_through_blocks("0.OsCi6`8oaNdL~)e{=.", full_sb3, mode="parent")
    assert type(result) == list
    assert result == ["0.OsCi6`8oaNdL~)e{=.", "/T~TiqeE4Xip(IQA6gZz"]