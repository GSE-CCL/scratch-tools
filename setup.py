import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ccl_scratch_tools",
    version="0.1.8",
    author="Creative Computing Lab",
    author_email="jarchibald@college.harvard.edu",
    description="Tools with which to work with Scratch JSON files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GSE-CCL/scratch-tools",
    project_urls={
        "Documentation": "https://ccl-scratch-tools.readthedocs.io/en/latest/"
    },
    packages=["ccl_scratch_tools", "ccl_scratch_tools.scratch_to_blocks"],
    install_requires=[
        "bs4",
        "jsonschema",
        "requests"
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education"
    ],
    python_requires='>=3.7'
)