import argparse
import json
import io
import os
import requests
import zipfile

class Scraper():
    """A scraper with which to scrape Scratch projects.

    Typical usage example:

      from ccl_scratch_tools import Scraper
        
      scraper = Scraper()
      
      project = scraper.download_project(555555555)
    """

    def __init__(self, studio_url = None, project_url = None):
        """Initializes scraper with studio and project URLs."""
        if studio_url is None:
            self.STUDIO_URL = "https://api.scratch.mit.edu/studios/{0}/projects?limit=40&offset={1}"
        else:
            self.STUDIO_URL = studio_url

        if project_url is None:
            self.PROJECT_URL = "https://projects.scratch.mit.edu/{0}"
        else:
            self.PROJECT_URL = project_url

    def download_project(self, id):
        """Downloads an individual project JSON and returns it as a Python object.
        
        Args:
            id: An integer Scratch project ID.

        Returns:
            A dictionary object representing the Scratch project JSON.

        Raises:
            RuntimeError: An error occurred accessing the Scratch API, or
                the project couldn't be downloaded in/converted to JSON format.
        """
        url = self.PROJECT_URL.format(id)
        r = requests.get(url)

        if r.status_code != 200:
            raise RuntimeError("GET {0} failed with status code {1}".format(url, r.status_code))

        project = ""
        try:
            project = r.json()
        except:
            # In some cases, a binary archive will download -- handle that
            if json.decoder.JSONDecodeError:
                try:
                    f = io.BytesIO(r.content)
                    archive = zipfile.ZipFile(f)
                    if "project.json" in archive.namelist():
                        proj = archive.read("project.json")
                        project = json.loads(proj.decode("utf-8"))
                except:
                    raise RuntimeError("Cannot handle format of project {0}".format(id))
        return project

    def download_projects(self, ids, projects_to_studio=dict(), output_directory=None, file_name=None):
        """Given project IDs, download the JSON files.
        
        Args:
            ids: array-like collection of Scratch project IDs.
            projects_to_studio: dictionary mapping project IDs to studio IDs.
                If set, creates subdirectories for each studio.
            output_directory (str): directory for output; if not set,
                defaults to current working directory.
            file_name (str): if set, combines projects into one JSON file with file_name;
                else creates a separate JSON file for each project.

        Returns:
            None.
        """
        if output_directory is None:
            output_directory = os.getcwd()

        self.make_dir(output_directory)
        projects = list()
        for id in ids:
            project = self.download_project(id)

            if len(project) < 1:
                break
            
            if file_name is None:
                od = output_directory
                if len(projects_to_studio) > 0:
                    od = "{0}/{1}".format(od, projects_to_studio[id])
                    self.make_dir(od)

                with open("{0}/{1}.json".format(od, id), "w") as f:
                    json.dump(project, f)
            else:
                projects.append(project)

        # If projects has at least one item, we should write to a single file
        if len(projects) > 0 and file_name is not None:
            with open("{0}/{1}".format(output_directory, file_name), "w") as f:
                json.dump(projects, f)

    def get_id(self, url):
        """Returns the integer ID from a string that may be a URL or an ID.
        
        Args:
            url: The string representing the URL, or ID, to be extracted.

        Returns:
            An integer ID of a Scratch object, whether a studio or project.

            In case of error, returns None.
        """
        url = url.rstrip()
        a = url.rstrip("/")
        try:
            return int(a.split("/")[-1])
        except:
            return None

    def get_ids_from_file(self, filename):
        """Returns a list of IDs from a newline-separated file.
            Project/studio link agnostic. Works with links and IDs.
        
        Args:
            filename: String file name of a text file with line-separated URLs or IDs.

        Returns:
            A list of integer IDs. Empty if error reading file.
        """
        ids = list()
        try:
            ids = list()
            with open(filename) as f:
                for l in f.readlines():
                    ids.append(self.get_id(l))
        except:
            pass
        return ids

    def get_projects_in_studio(self, id):
        """Returns the set of project IDs contained in a given Scratch studio.
        
        Args:
            id: An integer Scratch studio ID.
            
        Returns:
            A set of project IDs.

        Raises:
            RuntimeError: An error occurred accessing the Scratch API.
        """
        offset = 0
        project_ids = set()
        while True:
            url = self.STUDIO_URL.format(id, offset)
            r = requests.get(url)

            if r.status_code != 200:
                raise RuntimeError("GET {0} failed with status code {1}".format(url, r.status_code))

            # No more projects
            projects = r.json()
            if len(projects) < 1:
                break
            else:
                for project in projects:
                    project_ids.add(project["id"])
                offset += 40
            
        return project_ids
    
    def make_dir(self, path):
        """Creates a directory given path.
        
        Args:
            path (str): A file path on the current system.

        Returns:
            True, if directory was successfully created or already existed.

        Raises:
            RuntimeError: Failed to create the directory.
        """
        try:
            os.mkdir(path)
        except OSError:
            if FileExistsError:
                return True
            else:
                raise RuntimeError("Creation of directory '{0}' failed".format(path))
        else:
            return True
