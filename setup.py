import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccl_scratch_scrape",
    version="0.0.2",
    author="Creative Computing Lab",
    author_email="jarchibald@college.harvard.edu",
    description="Tools by which to scrape Scratch JSON files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GSE-CCL/scratch-studio-scrape",
    packages=setuptools.find_packages(),
    install_requires=[
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)