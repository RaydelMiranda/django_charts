import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Djando Charts",
    version="0.0.1",
    author="Raydel Miranda",
    author_email="raydel.miranda.gomez@gmail.com",
    description="App for charts generation for django apps.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/elasbit/fc-cloudtrails-sdk-py/src/develop/",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 2",
        "Operating System :: OS Independent",
    ),
)
