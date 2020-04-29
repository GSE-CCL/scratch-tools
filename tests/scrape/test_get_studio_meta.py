import pytest

def test_get_studio_meta_nonexistent(scraper):
    result = scraper.get_studio_meta(0)
    assert result is None

def test_get_studio_meta(scraper):
    result = scraper.get_studio_meta(26211962)

    assert type(result) == dict
    assert result["id"] == 26211962
    assert result["title"] == "Test_Studio"