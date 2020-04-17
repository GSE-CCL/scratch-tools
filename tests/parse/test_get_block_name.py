import pytest

def test_get_block_name_nonexistent(parser):
    result = parser.get_block_name("scratch_nonexistent")
    assert result is None

def test_get_block_name_categories(parser):
    tests = [
        ["motion_turnleft", "Turn Left"],
        ["control_if", "If"],
        ["event_whenbackdropswitchesto", "When Backdrop Switches To"],
        ["looks_nextcostume", "Next Costume"],
        ["operator_equals", "Equals"],
        ["sensing_keypressed", "Key Pressed"],
        ["sound_volume", "Volume"],
        ["procedures_call", "Block Call"],
        ["data_changevariableby", "Change Variable By"]
    ]

    for test in tests:
        assert parser.get_block_name(test[0]) == test[1]
