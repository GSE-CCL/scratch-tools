import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccl_scratch_tools",
    version="0.0.6",
    author="Creative Computing Lab",
    author_email="jarchibald@college.harvard.edu",
    description="Tools by which to work with Scratch JSON files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GSE-CCL/scratch-tools",
    project_urls={
        "Documentation": "https://ccl-scratch-tools.readthedocs.io/en/latest/"
    },
    packages=setuptools.find_packages(),
    install_requires=[
        "jsonschema",
        "requests"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)