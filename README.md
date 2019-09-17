# git-upm-publisher
Automate UPM package releases for Git repositories containing Unity plugins.

* **config_maker.py**: searches for *package.jso*n files within a repository, and saves the selected one to a *config.json* file
* **package_json_creator.py**: creates a *package.json* file from scratch
* **package_json_updater.py**: updates an existing *package.json* partially (or completely)
* **upm_publisher.py**: automates the whole UPM publishing process explained here: https://www.patreon.com/posts/25070968
* **main.py**: runs all the necessary modules in order, so you don't have to

This application uses [git-snapshot command from mob-sakai](https://www.npmjs.com/package/git-snapshot) in its **upm_publisher** module. Take a look and give them some love.
