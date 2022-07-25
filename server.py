import os

from os import getcwd, listdir
from tomlstore import toml_to_dict, store_object_as_toml

class TomlServer:

    def __init__(self, path: str = f"{getcwd()}/objects"):
        self.path = path

        self.metadata_path = f"{self.path}/#object_storage_data.toml"
        if os.path.exists(self.metadata_path):
            self.storage_data = toml_to_dict(self.metadata_path)
        else:
            self.storage_data = {}

    def store(self, d: dict):
        pass

    def retrieve(self, name: str):
        pass
