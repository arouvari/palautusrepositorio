from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        project_data = toml.loads(content)
        
        poetry_info = project_data.get('tool', {}).get('poetry', {})
        name = poetry_info.get('name', 'Test name')
        description = poetry_info.get('description', 'Test description')
        license = poetry_info.get('license', 'No license specified')
        authors = poetry_info.get('authors', [])
        dependencies = list(project_data.get('tool', {}).get('poetry', {}).get('dependencies', {}).keys())
        dev_dependencies = list(project_data.get('tool', {}).get('poetry', {}).get('group', {}).get('dev', {}).get('dependencies', {}).keys())


        return Project(name, description, license, authors, dependencies, dev_dependencies)
