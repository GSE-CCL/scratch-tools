import pytest

def test_get_id_from_urls(scraper):
    tests = {
        "https://scratch.mit.edu/projects/383948574/": 383948574,
        "https://scratch.mit.edu/projects/383948574": 383948574
    }

    for test in tests:
        assert scraper.get_id(test) == tests[test]

def test_get_id_from_rel_urls(scraper):
    tests = {
        "383948574/": 383948574,
        "383948574": 383948574,
        "/projects/383948574": 383948574
    }

    for test in tests:
        assert scraper.get_id(test) == tests[test]

def test_get_id_invalid_input(scraper):
    tests = {
        "/projects/": None,
        "https://scratch.mit.edu/": None,
        "https://scratch.mit.edu/projects/383948574/editor": None
    }

    for test in tests:
        assert scraper.get_id(test) == tests[test]