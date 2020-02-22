import argparse
import json
import io
import os
import requests
import zipfile

import helpers

STUDIO_URL = "https://api.scratch.mit.edu/studios/{0}/projects?limit=40&offset={1}"
PROJECT_URL = "https://projects.scratch.mit.edu/{0}"

def get_projects_in_studio(id):
    """Given integer studio ID, return a set of integer project IDs"""
    offset = 0
    project_ids = set()
    while True:
        url = STUDIO_URL.format(id, offset)
        r = requests.get(url)

        if r.status_code != 200:
            raise RuntimeError("GET {0} failed with status code {1}".format(r.status_code, url))

        # No more projects
        projects = r.json()
        if len(projects) < 1:
            break
        else:
            for project in projects:
                project_ids.add(project["id"])
            offset += 40
        
    return project_ids


def download_project(id):
    """Download an individual project and return its Python object"""
    url = PROJECT_URL.format(id)
    r = requests.get(url)

    if r.status_code != 200:
        raise RuntimeError("GET {0} failed with status code {1}".format(r.status_code, url))

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
                print("Cannot handle project {0}".format(id))
    return project


def download_projects(ids, output_directory=os.getcwd(), file_name=None):
    """"Given project IDs, download the JSON files.
        :param ids: array-like collection of Scratch project IDs
        :param output_directory: directory for output
        :param file_name: if blank, creates a separate JSON file
                          for each project; otherwise, combines
                          projects into one JSON file with file_name"""

    helpers.make_dir(output_directory)
    projects = list()
    for id in ids:
        project = download_project(id)

        if len(project) < 1:
            break
        
        if file_name is None:
            with open("{0}/{1}.json".format(output_directory, id), "w") as f:
                json.dump(project, f)
        else:
            projects.append(project)

    # If projects has at least one item, we should write to a single file
    if len(projects) > 0 and file_name is not None:
        with open("{0}/{1}.json".format(output_directory, file_name), "w") as f:
            json.dump(projects, f)


def get_arguments():
    parser = argparse.ArgumentParser(description="Download Scratch projects.")

    # Arguments related to input
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("-s", dest="studio", nargs="*", help="Studio ID. Will scrape all projects from the studio with the given ID.")
    inputs.add_argument("-p", dest="project", nargs="*", help="Project ID. Will scrape one project for each ID provided.")
    inputs.add_argument("-f", dest="studio_list", nargs="*", help="File name for a line-separated list of studio URLs (or IDs). Will scrape all projects in all studios.")
    inputs.add_argument("-g", dest="project_list", nargs="*", help="File name for a line-separated list of project URLs (or IDs). Will scrape all projects.")

    # Arguments related to output
    parser.add_argument("-d", dest="output_directory", help="Output directory. Will save output to this directory, and create the directory if doesn’t exist.")
    parser.add_argument("-n", dest="output_name", help="Name of the output JSON file, if only a single output file is desired. Otherwise, will save projects to individual JSON files.")

    return parser.parse_args()


def get_ids_from_file(filename):
    """Given a filename, return a list of IDs from a newline-separated file. Project/studio link agnostic."""
    ids = list()
    try:
        ids = list()
        with open(filename) as f:
            for l in f.readlines():
                ids.append(helpers.get_id(l))
    except:
        pass
    return ids


def get_project_ids(arguments):
    """Given input arguments, return a set of all the project IDs."""
    projects = list()
    if arguments.project is not None:
        projects = arguments.project
    elif arguments.studio is not None:
        for s in arguments.studio:
            projects += get_projects_in_studio(helpers.get_id(s))
    elif arguments.project_list is not None:
        for p in arguments.project_list:
            projects += get_ids_from_file(p)
    elif arguments.studio_list is not None:
        for s in arguments.studio_list:
            studios = get_ids_from_file(s)
            for studio in studios:
                projects += get_projects_in_studio(studio)

    return set(projects)


def main():
    arguments = get_arguments()
    projects = get_project_ids(arguments)

    if arguments.output_directory is None:
        download_projects(projects, file_name=arguments.output_name)
    else:
        download_projects(projects, output_directory=arguments.output_directory, file_name=arguments.output_name)


if __name__ == "__main__":
    main()