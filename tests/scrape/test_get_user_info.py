import pytest

def test_get_user_info_nonexistent(scraper):
    with pytest.raises(RuntimeError):
        scraper.get_user_info("jsarchibald_doesnotexist")

def test_get_user_info(scraper):
    result = scraper.get_user_info("jsarchibald")

    assert type(result) == dict
    assert result["id"] == 56916655
    assert result["username"] == "jsarchibald"
