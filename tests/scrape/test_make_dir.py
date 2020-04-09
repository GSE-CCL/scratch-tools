import pytest

def test_new_dir(scraper, tmp_path):
    path = tmp_path.joinpath("test_directory")

    assert scraper.make_dir(str(path))
    assert path.exists()
    assert path.is_dir()

def test_exists(scraper, tmp_path):
    path = tmp_path.joinpath("test_directory")
    
    assert scraper.make_dir(str(path))
    assert scraper.make_dir(str(path))
    assert path.exists()
    assert path.is_dir()