import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="git-upm-publisher",
    version="0.0.5",
    author="starikcetin <cetinsamedtarik@gmail.com> (https://github.com/starikcetin)",
    author_email="cetinsamedtarik@gmail.com",
    description="Automate UPM package releases for Git repositories containing Unity plugins.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/starikcetin/git-upm-publisher",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'gup = git_upm_publisher.main:main',
            'gup-main = git_upm_publisher.main:main',
            'gup-config-maker = git_upm_publisher.config_maker:main',
            'gup-package-json-creator = git_upm_publisher.package_json_creator:main',
            'gup-package-json-updater = git_upm_publisher.package_json_updater:main',
            'gup-upm-publisher = git_upm_publisher.upm_publisher:main',
        ],
    },
)
