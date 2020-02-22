import os

def get_id(url):
    """Get the ID from a string that may be a URL or the ID alone"""
    url = url.rstrip()
    a = url.rstrip("/")
    try:
        return int(a.split("/")[-1])
    except:
        return None

def make_dir(path):
    """os.mkdir wrapper with error checking"""
    try:
        os.mkdir(path)
    except OSError:
        if FileExistsError:
            return True
        else:
            raise Exception("Creation of directory failed")
    else:
        return True
