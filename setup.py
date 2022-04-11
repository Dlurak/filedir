from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Filedir is a python module to work with files and directories.'
with open('README.md', 'r') as f:
    LONG_DESCRIPTION = f.read()

# Setting up
setup(
    name="filedir",
    version=VERSION,
    author="Dlurak",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    keywords=['python', 'files', 'directorys', 'folders', 'sorting'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
    ]
)