import pytest

def test_get_id_from_file_projects(scraper):
    results = scraper.get_ids_from_file("tests/fixtures/projects.txt")

    assert type(results) == list
    assert len(results) == 10
    assert results == [236422889, 237070059, 235792107, 236007150, 235790063, 355340020, 236062452, 235835130, 236142330, 361054763]

def test_get_id_from_file_studios(scraper):
    results = scraper.get_ids_from_file("tests/fixtures/studios.txt")

    assert type(results) == list
    assert len(results) == 4
    assert results == [5142687, 5142688, 5142689, 5142691]

def test_get_id_from_file_nonexistent_file(scraper):
    results = scraper.get_ids_from_file("tests/fixtures/nonexistent.txt")

    assert type(results) == list
    assert len(results) == 0
    assert results == []