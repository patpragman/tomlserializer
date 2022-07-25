import toml
from os import path, getcwd


def store_object_as_toml(d: dict, filepath: str = f"{getcwd()}/objects/obj.toml") -> None:
    """
    takes a dictionary "d" and stores it at filepath

    :param filepath: the path of the file
    :param d: the dictionary d
    :return: None - this just stores the dictionary, it doesn't return anything
    """
    file_name = filepath
    with open(filepath, "w") as toml_file:
        toml_file.write(toml.dumps(d))


def toml_to_dict(filepath: str = f"{getcwd()}/objects/obj.toml") -> dict:
    """
    takes a path and returns a dictionary of from toml file

    :param filepath: the path to the toml file
    :return: the dictionary file
    """
    file_name = filepath
    with open(file_name, "r") as toml_file:
        d = toml.load(toml_file)

    return d
