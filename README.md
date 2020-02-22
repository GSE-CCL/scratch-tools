# scratch-studio-scrape
A batch downloader for Scratch studios' project JSON files, developed for the Creative Computing Lab at the Harvard Graduate School of Education.

## Usage

Usage: scrape.py [options]

- -h: Usage help.

Inputs:

- -s: Studio ID. Will scrape all projects from the studio with the given ID.
- -p: Project ID. Will scrape one project for each ID provided.
- -f: File name for a line-separated list of studio URLs (or IDs). Will scrape all projects in all studios.
- -g: File name for a line-separated list of project URLs (or IDs). Will scrape all projects.

Outputs:

- -d: Output directory. Will save output to this directory, and create the directory if doesn’t exist.
- -n: Name of the output JSON file, if only a single output file is desired. Otherwise, will save projects to individual JSON files.

## Resources
[https://github.com/LLK/scratch-rest-api/wiki/](https://github.com/LLK/scratch-rest-api/wiki/) for API documentation

[https://api.scratch.mit.edu/studios/{ID}/projects](https://api.scratch.mit.edu/studios/{ID}/projects) to get a list of all the projects, with IDs and descriptions

[https://projects.scratch.mit.edu/{ID}](https://projects.scratch.mit.edu/{ID}) to download project JSON
