import pytest
import sys
import os

sys.path.insert(0, os.path.abspath('../../ccl_scratch_tools'))
from scrape import Scraper


@pytest.fixture
def scraper():
    return Scraper()

@pytest.fixture
def project_list():
    with open("../fixtures/projects.txt") as f:
        return list(f.readlines())

@pytest.fixture
def studio_list():
    with open("../fixtures/studios.txt") as f:
        return list(f.readlines())

@pytest.fixture
def test_studio():
    scrape = Scraper()
    projects = scrape.get_projects_in_studio(26211962)

    p_to_s = dict()
    for project in projects:
        p_to_s[project] = 26211962

    return projects, p_to_s