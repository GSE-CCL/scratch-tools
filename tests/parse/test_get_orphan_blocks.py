import pytest

def test_get_orphan_blocks_nonexistent(parser):
    result = parser.get_orphan_blocks(dict())
    assert result == False

def test_get_orphan_blocks_empty(parser, empty_sb3):
    result = parser.get_orphan_blocks(empty_sb3)
    assert type(result) == set
    assert len(result) == 0

def test_get_orphan_blocks_four(parser, orphans_sb3):
    result = parser.get_orphan_blocks(orphans_sb3)
    assert type(result) == set
    assert len(result) == 4
    assert result == {"712qz)/NOaL]g*)U(O7y", "rHQZ~$.G@u#^MG2~WYK}", "*EiVC/-!#?8R@AO[Fjl]", "2K!##3[o$uXXA.YCyUzN"}
