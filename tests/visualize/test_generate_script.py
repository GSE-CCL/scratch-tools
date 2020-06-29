import pytest

def test_generate_script_no_blocks(visualizer):
    result = visualizer.generate_script("fakeid", list())
    assert result == False

def test_generate_script_no_blocks_text(visualizer):
    result = visualizer.generate_script("fakeid", list(), text=True)
    assert result == False

def test_generate_script_nonexistent(visualizer, full_sb3):
    result = visualizer.generate_script("fakeid", full_sb3["targets"][0]["blocks"])
    assert result == False

def test_generate_script_nonexistent_text(visualizer, full_sb3):
    result = visualizer.generate_script("fakeid", full_sb3["targets"][0]["blocks"], text=True)
    assert result == False

def test_generate_script_exists(parser, visualizer, full_sb3):
    target, _ = parser.get_target("q3cBGj=%#c^E;eayaZs6", full_sb3)
    result = visualizer.generate_script("q3cBGj=%#c^E;eayaZs6", target["blocks"])

    assert result == {'label': 'play sound (Sound! v) until done'}

def test_generate_script_exists_text(parser, visualizer, full_sb3):
    target, _ = parser.get_target("q3cBGj=%#c^E;eayaZs6", full_sb3)
    result = visualizer.generate_script("q3cBGj=%#c^E;eayaZs6", target["blocks"], text=True)
    
    assert result == "play sound (Sound! v) until done\n\n"
    
def test_generate_script_exists_limit(parser, visualizer, full_sb3):
    target, _ = parser.get_target("t0gCI_RcP^f%JiDTILyU", full_sb3)
    surrounding = parser.get_surrounding_blocks("t0gCI_RcP^f%JiDTILyU", full_sb3)
    result = visualizer.generate_script(surrounding[0], target["blocks"], surrounding)
    
    assert result == {'label': 'define test_function', 'next': {'label': 'ask [Question] and wait', 'next': {'label': 'if <(answer) > [50]> then', 'substack': {'label': 'set [test_variable v] to (pick random (1) to (10))', 'next': {'label': 'play sound (Sound! v) until done'}}}}}

def test_generate_script_starts_with_input(parser, visualizer, full_sb3):
    """Should fail since we are forcing scratch-to-blocks to use an INPUT to start."""

    target, _ = parser.get_target("LFsgr8N^R^kVy-c66YJ8", full_sb3)

    with pytest.raises(Exception):
        surrounding = parser.get_surrounding_blocks("LFsgr8N^R^kVy-c66YJ8", full_sb3, 2)
        result = visualizer.generate_script(surrounding[0], target["blocks"], surrounding, find_block=False)

def test_generate_script_nostart_with_input(parser, visualizer, full_sb3):
    """Should succeed since we're letting scratch-to-blocks find the closest BLOCK it can."""

    target, _ = parser.get_target("LFsgr8N^R^kVy-c66YJ8", full_sb3)
    surrounding = parser.get_surrounding_blocks("LFsgr8N^R^kVy-c66YJ8", full_sb3, 2)
    result = visualizer.generate_script(surrounding[0], target["blocks"], surrounding)
