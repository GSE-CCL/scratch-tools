import pytest

def test_get_target_empty(visualizer):
    result = visualizer.get_target("fakeid", dict())
    assert result == False

def test_get_target_nonexistent(visualizer, full_sb3):
    result = visualizer.get_target("fakeid", full_sb3)
    assert result == False

def test_get_target_exists(visualizer, full_sb3):
    result = visualizer.get_target("CupN)`F`z1tugXtDqYzj", full_sb3)
    assert result[0]["name"] == "Scratch"
    assert result[1] == 1
