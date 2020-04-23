import pytest

def test_get_project_meta_nonexistent(scraper):
    with pytest.raises(RuntimeError):
        scraper.get_project_meta(0)

def test_get_project_meta(scraper):
    result = scraper.get_project_meta(383948574)

    assert type(result) == dict
    assert result["id"] == 383948574
    assert result["title"] == "Test_Full"
    assert result["public"]