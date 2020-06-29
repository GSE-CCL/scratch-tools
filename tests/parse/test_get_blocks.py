import pytest

def test_get_blocks_nonexistent(parser):
    result = parser.get_blocks(dict())
    assert result == False

def test_get_blocks_empty(parser, empty_sb3):
    result = parser.get_blocks(empty_sb3)
    assert type(result) == dict
    assert len(result) == 0
    assert result == {}

def test_get_blocks_full(parser, full_sb3):
    result = parser.get_blocks(full_sb3)
    assert type(result) == dict
    assert len(result) == 20
    lengths = {
        "event_whenflagclicked": 1,
        "control_wait": 1,
        "control_repeat": 1,
        "motion_movesteps": 1,
        "motion_ifonedgebounce": 1,
        "event_broadcast": 1,
        "data_showvariable": 1,
        "looks_nextcostume": 1,
        "looks_sayforsecs": 1,
        "event_whenbroadcastreceived": 1,
        "sound_changevolumeby": 1,
        "procedures_call": 1,
        "procedures_definition": 1,
        "sensing_askandwait": 1,
        "control_if": 1,
        "operator_gt": 1,
        "sensing_answer": 1,
        "data_setvariableto": 1,
        "operator_random": 1,
        "sound_playuntildone": 1
    }
    for block in result:
        assert len(result[block]) == lengths[block]

def test_get_blocks_no_orphans(parser, orphans_sb3):
    result = parser.get_blocks(orphans_sb3, False)
    assert type(result) == dict
    assert len(result) == 2

def test_get_blocks_orphans(parser, orphans_sb3):
    result = parser.get_blocks(orphans_sb3)
    assert type(result) == dict
    assert len(result) == 6
