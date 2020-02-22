# Scratch Studio Scrape
A batch downloader for Scratch studios' project JSON files, developed for the Creative Computing Lab at the Harvard Graduate School of Education.

## Setup

1. Make sure you've installed Python 3 and Pip.
2. Navigate the terminal to the downloaded repository.
3. Run `pip install -r requirements.txt`.
4. You should be all set to run the code as described below.

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

## Examples

Scrape all projects from studio with id `ID_NUMBER`:

```python scrape.py -s ID_NUMBER```

Scrape the projects `ID_NUM1` and `ID_NUM2`:

```python scrape.py -p ID_NUM1 ID_NUM2```

Scrape all the projects listed in `projects.txt`:

```python scrape.py -g projects.txt```

Scrape all the projects from all the studios listed in `studios.txt`:

```python scrape.py -f studios.txt```

Do the same as previously, but save all the projects to a directory `output`:

```python scrape.py -f studios.txt -d output```

Do the same thing, but save all the projects in one JSON file, `out.json`, in the directory `output`:

```python scrape.py -f studios.txt -d output -n out```

## Resources
[https://github.com/LLK/scratch-rest-api/wiki/](https://github.com/LLK/scratch-rest-api/wiki/) for API documentation

[https://api.scratch.mit.edu/studios/{ID}/projects](https://api.scratch.mit.edu/studios/{ID}/projects) to get a list of all the projects, with IDs and descriptions

[https://projects.scratch.mit.edu/{ID}](https://projects.scratch.mit.edu/{ID}) to download project JSON
