import pytest

def test_get_block_names_nonexistent_opcodes(parser):
    result = parser.get_block_names(["scratch_nonexistent"])
    assert result == [None]

def test_get_block_names_nonexistent_blockids(parser, empty_sb3):
    result = parser.get_block_names(["scratch_nonexistent"], scratch_data=empty_sb3)
    assert result == [None]

def test_get_block_names_opcodes(parser):
    test = [
        "motion_turnleft",
        "control_if",
        "event_whenbackdropswitchesto",
        "looks_nextcostume",
        "operator_equals",
        "sensing_keypressed",
        "sound_volume",
        "procedures_call",
        "data_changevariableby"
    ]
    answer = [
        "Turn Left",
        "If",
        "When Backdrop Switches To",
        "Next Costume",
        "Equals",
        "Key Pressed",
        "Volume",
        "Block Call",
        "Change Variable By"
    ]

    result = parser.get_block_names(test)
    assert len(result) == 9
    assert result == answer

def test_get_block_names_categories(parser):
    test = [
        "motion_turnleft",
        "control_if",
        "event_whenbackdropswitchesto",
        "looks_nextcostume",
        "operator_equals",
        "sensing_keypressed",
        "sound_volume",
        "procedures_call",
        "data_changevariableby"
    ]
    answer = [
        "Turn Left",
        "If",
        "When Backdrop Switches To",
        "Next Costume",
        "Equals",
        "Key Pressed",
        "Volume",
        "Block Call",
        "Change Variable By"
    ]

    result = parser.get_block_names(test)
    assert len(result) == 9
    assert result == answer

def test_get_block_names_opcodes(parser):
    test = [
        "motion_turnleft",
        "control_if",
        "event_whenbackdropswitchesto",
        "looks_nextcostume",
        "operator_equals",
        "sensing_keypressed",
        "sound_volume",
        "procedures_call",
        "data_changevariableby"
    ]
    answer = [
        "Turn Left",
        "If",
        "When Backdrop Switches To",
        "Next Costume",
        "Equals",
        "Key Pressed",
        "Volume",
        "Block Call",
        "Change Variable By"
    ]

    result = parser.get_block_names(test)
    assert len(result) == 9
    assert result == answer

def test_get_block_names_blockids(parser, full_sb3):
    test = [
        "CupN)`F`z1tugXtDqYzj",
        "Fw-*+6_[m%^1H#z%J9:5",
        "*@ClP%]SM`L.}J;jo{:N"
    ]
    answer = [
        "Repeat",
        "Say for Secs",
        "Random"
    ]

    result = parser.get_block_names(test, scratch_data=full_sb3)
    assert len(result) == 3
    assert result == answer
