This package is deprecated in favor of [git-upm-publisher-2](https://github.com/starikcetin/git-upm-publisher-2).

The new package is written in Typescript. It is much more stable and doesn't have the annoying package resolution bugs of python.

---

# git-upm-publisher

Automate UPM package releases for Git repositories containing Unity plugins.

## Modules

- **config_maker.py**: searches for *package.jso*n files within a repository, and saves the selected one to a _config.json_ file
- **package_json_creator.py**: creates a _package.json_ file from scratch
- **package_json_updater.py**: updates an existing _package.json_ partially (or completely)
- **upm_publisher.py**: automates the whole UPM publishing process explained here: https://www.patreon.com/posts/25070968
- **main.py**: runs all the necessary modules in order, so you don't have to

## Installation

https://pypi.org/project/git-upm-publisher/

`pip install git-upm-publisher`

## Usage

Run `gup` in your command line.

### Advanced

- `gup-main` runs `main` (equaivalent of `gup`)
- `gup-config-maker` runs `config_maker`
- `gup-package-json-creator` runs `package_json_creator`
- `gup-package-json-updater` runs `package_json_updater`
- `gup-upm-publisher` runs `upm_publisher`

## License

MIT license. Refer to the [LICENSE](/LICENSE) file.
Copyright (c) 2019 S. Tarık Çetin

This application uses [git-snapshot command from mob-sakai](https://www.npmjs.com/package/git-snapshot).
Take a look and give them some love.
