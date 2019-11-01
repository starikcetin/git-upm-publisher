import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-upm-publisher",
    version="0.0.1",
    author="starikcetin <cetinsamedtarik@gmail.com> (https://github.com/starikcetin)",
    author_email="cetinsamedtarik@gmail.com",
    description="Automate UPM package releases for Git repositories containing Unity plugins.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/starikcetin/git-upm-publisher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
