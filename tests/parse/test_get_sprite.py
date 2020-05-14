import pytest

def test_get_sprite_nodata(parser):
    result = parser.get_sprite("fakeid", dict())
    assert result == False

def test_get_sprite_nonexistent(parser, full_sb3):
    result = parser.get_sprite("fakeid", full_sb3)
    assert result == False

def test_get_sprite(parser, full_sb3):
    result = parser.get_sprite("CupN)`F`z1tugXtDqYzj", full_sb3)
    assert type(result) == dict
    assert result == {
        "index": 1,
        "name": "Scratch",
        "costume_asset": "e6ddc55a6ddd9cc9d84fe0b4c21e016f",
        "costume_asset_url": "https://assets.scratch.mit.edu/internalapi/asset/e6ddc55a6ddd9cc9d84fe0b4c21e016f.svg/get/"
    }
    