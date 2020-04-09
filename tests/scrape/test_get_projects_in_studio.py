import pytest

def test_get_projects_in_studio_nonexistent(scraper):
    with pytest.raises(RuntimeError):
        scraper.get_projects_in_studio(-1)

def test_download_project(scraper):
    result = scraper.get_projects_in_studio(26211962)
    
    assert type(result) == set
    assert len(result) == 2
    assert result == {383948574, 383948531}
    