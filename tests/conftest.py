import json
import os
import pytest
import sys

sys.path.insert(0, os.path.abspath('../ccl_scratch_tools'))
from parse import Parser
from scrape import Scraper


@pytest.fixture
def parser():
    return Parser()

@pytest.fixture
def empty_sb3():
    with open("fixtures/empty.json") as f:
        return dict(json.load(f))

@pytest.fixture
def full_sb3():
    with open("fixtures/full.json") as f:
        return dict(json.load(f))

@pytest.fixture
def project_list():
    with open("fixtures/projects.txt") as f:
        return list(f.readlines())

@pytest.fixture
def studio_list():
    with open("fixtures/studios.txt") as f:
        return list(f.readlines())

@pytest.fixture
def scraper():
    return Scraper()

@pytest.fixture
def test_studio():
    scrape = Scraper()
    projects = scrape.get_projects_in_studio(26211962)

    p_to_s = dict()
    for project in projects:
        p_to_s[project] = 26211962

    return projects, p_to_s
