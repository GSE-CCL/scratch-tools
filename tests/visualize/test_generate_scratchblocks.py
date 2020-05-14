import pytest

def test_generate_scratchblocks_nonexistent(visualizer):
    result = visualizer.generate_scratchblocks(dict())
    assert result == False

def test_generate_scratchblocks_empty(visualizer, empty_sb3):
    result = visualizer.generate_scratchblocks(empty_sb3)

    assert result == list()

def test_generate_scratchblocks_full(visualizer, full_sb3):
    result = visualizer.generate_scratchblocks(full_sb3)

    assert result[1] == {'label': 'when I receive [message1 v]', 'next': {'label': 'change volume by (-10)', 'next': {'label': 'test_function'}}}
