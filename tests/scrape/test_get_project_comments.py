import pytest

def test_get_project_comments_nonexistent(scraper):
    with pytest.raises(RuntimeError):
        scraper.get_project_meta(0)

def test_get_project_comments_empty(scraper):
    assert scraper.get_project_comments(383948531) == list()

def test_get_project_comments_full(scraper):
    result = scraper.get_project_comments(383948574)
    partial_result = {"username": "jsarchibald", "comment": "I love this project!", "timestamp": "2020-04-22T21:17:47Z"}

    assert type(result) == list

    # It is public, so people could add more I guess
    assert len(result) >= 3
    assert partial_result in result