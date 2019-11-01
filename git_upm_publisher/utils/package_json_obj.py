class PackageJsonObj:
    def init_with_values(self, package_name: str, display_name: str, unity_min_version: str, description: str,
                         version: str, dependencies: dict):
        self.name = package_name
        self.displayName = display_name

        if unity_min_version != "":
            self.unity = unity_min_version

        self.description = description
        self.version = version
        self.dependencies = dependencies

    def init_from_dict(self, init_dict: dict):
        for key in init_dict:
            setattr(self, key, init_dict[key])

    def get(self, name):
        return getattr(self, name)

    def set(self, name, value):
        setattr(self, name, value)