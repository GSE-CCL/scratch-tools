import pytest

def test_get_block_text_nodata(parser):
    result = parser.get_block_text(dict())
    assert result == False

def test_get_block_text_empty(parser, empty_sb3):
    result = parser.get_block_text(empty_sb3)
    assert type(result) == dict
    assert result == {}

def test_get_block_text_full(parser, user_text_sb3):
    result = parser.get_block_text(user_text_sb3)
    assert type(result) == dict
    assert result == {
        "saying for a period": ["u=ko6`@{_S2ll5(ET9di"], 
        "just saying something": ["5Qr9`yk:%tgB!fk3`mh1"],
        "thinking for a period": ["$orHuK2~}2lhFM,m/_:k"],
        "just thinking something": ["XX[QKwrRYARGI$~=tzc%"],
        "asking the user a question": ["8;/H2IHaAV:pHqFiStQu"]
    }

def test_get_block_text_repeat(parser, user_text_repeat_sb3):
    result = parser.get_block_text(user_text_repeat_sb3)
    assert type(result) == dict
    assert result == {
        "Hello!": ['F_)LdBN*E8;!Mmo3q/~X', '9TCb4I,IMA@irRid[7f~'],
        "Hmm...": ['X]@a#cxYkFjgv;;YqBNJ', 'oRdAVdkk*`!nQR3^2/?v']
    }
