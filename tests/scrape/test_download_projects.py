import os
import pytest

def test_download_project_default(scraper, test_studio, tmp_path):
    projects, p_to_s = test_studio
    original_dir = os.getcwd()
    os.chdir(str(tmp_path))

    result = scraper.download_projects(projects)
    os.chdir(original_dir)

    assert result == None

    # Test project existence
    for project in projects:
        file_path = tmp_path.joinpath(str(project) + ".json")

        assert file_path.exists()
        assert file_path.is_file()
        assert file_path.stat().st_size > 0
        
def test_download_project_studio_subdirs(scraper, test_studio, tmp_path):
    projects, p_to_s = test_studio
    original_dir = os.getcwd()
    os.chdir(str(tmp_path))

    result = scraper.download_projects(projects, p_to_s)
    os.chdir(original_dir)

    assert result == None

    # Test studio subdirectory exists
    file_path = tmp_path.joinpath(str(p_to_s[list(p_to_s.keys())[0]]))
    assert file_path.exists()
    assert file_path.is_dir()

    # Test project existence
    for project in projects:
        fp = file_path.joinpath(str(project) + ".json")
        assert fp.exists()
        assert fp.is_file()
        assert fp.stat().st_size > 0

def test_download_project_outputdir(scraper, test_studio, tmp_path):
    projects, p_to_s = test_studio
    original_dir = os.getcwd()
    os.chdir(str(tmp_path))

    result = scraper.download_projects(projects, output_directory="test")
    os.chdir(original_dir)
    file_path = tmp_path.joinpath("test")

    # Test output directory existence
    assert result == None
    assert file_path.exists()
    assert file_path.is_dir()

    # Test project existence
    for project in projects:
        fp = file_path.joinpath(str(project) + ".json")

        assert fp.exists()
        assert fp.is_file()
        assert fp.stat().st_size > 0

def test_download_project_onefile(scraper, test_studio, tmp_path):
    projects, p_to_s = test_studio
    original_dir = os.getcwd()
    os.chdir(str(tmp_path))

    result = scraper.download_projects(projects, file_name="test.json")
    os.chdir(original_dir)
    file_path = tmp_path.joinpath("test.json")

    # Test single output file existence
    assert result == None
    assert file_path.exists()
    assert file_path.is_file()
    assert file_path.stat().st_size > 0

def test_download_project_onefile_outputdir(scraper, test_studio, tmp_path):
    projects, p_to_s = test_studio
    original_dir = os.getcwd()
    os.chdir(str(tmp_path))

    result = scraper.download_projects(projects, output_directory="test", file_name="test.json")
    os.chdir(original_dir)
    file_path = tmp_path.joinpath("test")

    # Test output directory existence
    assert result == None
    assert file_path.exists()
    assert file_path.is_dir()

    # Test singular file output existence
    file_path = file_path.joinpath("test.json")
    assert file_path.exists()
    assert file_path.is_file()
    assert file_path.stat().st_size > 0

def test_download_project_studio_subdirs_outputdir(scraper, test_studio, tmp_path):
    projects, p_to_s = test_studio
    original_dir = os.getcwd()
    os.chdir(str(tmp_path))

    result = scraper.download_projects(projects, projects_to_studio=p_to_s, output_directory="test")
    os.chdir(original_dir)
    file_path = tmp_path.joinpath("test")

    # Test output directory existence
    assert result == None
    assert file_path.exists()
    assert file_path.is_dir()

    # Test project subdirectory existence
    file_path = file_path.joinpath(str(p_to_s[list(p_to_s.keys())[0]]))
    assert file_path.exists()
    assert file_path.is_dir()

    # Test project existence
    for project in projects:
        fp = file_path.joinpath(str(project) + ".json")
        assert fp.exists()
        assert fp.is_file()
        assert fp.stat().st_size > 0