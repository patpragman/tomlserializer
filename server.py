import os

from datetime import datetime
from os import getcwd, listdir, remove
from tomlstore import toml_to_dict, store_object_as_toml

class TomlServer:

    def __init__(self, path: str = f"{getcwd()}/objects"):
        self.path = path

        self.metadata_path = f"{self.path}/#object_storage_data.toml"
        if os.path.exists(self.metadata_path):
            self.storage_data = toml_to_dict(self.metadata_path)
        else:
            self.storage_data = {}

    def store(self, d: dict, name) -> None:
        store_object_as_toml(d, f"{self.path}/{name}")
        self.storage_data[name] = datetime.utcnow()

    def retrieve(self, name: str) -> dict:
        return toml_to_dict(f"{self.path}/{name}")

    def remove(self, name: str) -> None:
        remove(f"{self.path}/{name}")

    def __del__(self):
        store_object_as_toml(self.storage_data, self.metadata_path)
