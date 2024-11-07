class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __str__(self):
        authors_str = "\n".join([f"- {author}" for author in self.authors])
        dependencies_str = "\n".join([f"- {dependency}" for dependency in self.dependencies])
        dev_dependencies_str = "\n".join([f"- {dev_dependency}" for dev_dependency in self.dev_dependencies])

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n"
            f"\n"
            f"Authors:\n{authors_str}\n"
            f"\n"
            f"Dependencies:\n{dependencies_str}\n"
            f"\n"
            f"Development dependencies:\n{dev_dependencies_str}"
        )