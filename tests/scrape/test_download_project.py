import pytest

def test_download_project_nonexistent(scraper):
    with pytest.raises(RuntimeError):
        scraper.download_project(0)

def test_download_project(scraper):
    result = scraper.download_project(383948574)
    
    assert type(result) == dict