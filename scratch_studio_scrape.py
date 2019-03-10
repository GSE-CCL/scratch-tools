# NOTES:
# project link format: https://scratch.mit.edu/projects/245388250/
# project sb3 json download: https://projects.scratch.mit.edu/284824184
# BUG: some project jsons saving as empty files

import os
import requests
import json

def main():
    # directory for all studio information
    make_dir("studios")

    # get projects for every studio in studio_links.txt
    try:
        studio_links = open("studio_links.txt", "r")
    except FileNotFoundError:
        raise Exception("Please put all Scratch studio links, line separated, in a file named studio_links.txt")

    for idx, link in enumerate(studio_links):
        download_studio(link.rstrip(), idx + 1)

    studio_links.close()

def download_studio(link, studio_num):
    ''' downloads studio information and project jsons '''

    # download studio information (w/ all project ids)
    x = 0

    studio_file = open("studios/studio%i.json" % studio_num, "w")
    studio_file.write("[\n")

    print("Getting studio%i" % studio_num + " data......")
    # get 40 projects at a time until there are no projects left
    while True:
        r = requests.get("%sprojects?limit=40&offset=%i" % (link, x))

        if r.status_code != 200:
            # error
            raise ApiError('GET /api.scratch.mit.edu/ {}'.format(resp.status_code))

        # no more scratch projects
        if len(r.json()) == 0:
            break
        else:
            # studio_file contains all meta info about projects in the studio
            for proj in r.json():
                json.dump(proj, studio_file, ensure_ascii=False, indent=4)
                studio_file.write(",\n")
            x += 40

    # pesky extra ,\n at the end of last project
    studio_file.seek(studio_file.tell() - 2, os.SEEK_SET)
    studio_file.write("\n]")
    studio_file.close()

    # parse & extract project ids
    print("Parsing studio%i.json" % studio_num + " for project ids......")
    proj_ids = []

    with open('studios/studio%i.json' % studio_num) as f:
        studio_projs = json.load(f)
        for proj in studio_projs:
            proj_ids.append(proj["id"])

    # make a file that keeps track of project JSONs in studio folder
    proj_dir = open("studios/studio%i_project_ids.txt" % studio_num, "w")

    # get project JSONs, output to numbered studio_project folders
    make_dir("studio%i_projects" % studio_num)

    # get project JSONs by id
    print("Getting studio%i project JSONs by id......" % studio_num)
    for p_id in proj_ids:
        r = requests.get("https://projects.scratch.mit.edu/%i" % p_id)

        # this project is unaccessible
        if r.status_code != 200:
            raise ApiError('GET /projects.scratch.mit.edu/%i/ %i' % (p_id, format(resp.status_code)))

        # project successfully reached
        else:
            proj_file = open("studio%i_projects/%i.json" % (studio_num, p_id), "w")
            try:
                json.dump(r.json(), proj_file, ensure_ascii=False, indent=4)
                pass
            except Exception as e:
                print(">> %i.json cannot be opened" % p_id)

            # only write successfully downloaded project ids to this file
            proj_dir.write("%i\n" % p_id)

            proj_file.close()

    proj_dir.close()

def make_dir(path):
    ''' os.mkdir wrapper with error checking '''
    try:
        os.mkdir(path)
    except OSError:
        if FileExistsError:
            print("Directory %s already exists" % path)
        else:
            raise Exception("Creation of directory %s failed" % path)
    else:
        print("Successfully created directory %s" % path)

if __name__ == "__main__":
    main()
