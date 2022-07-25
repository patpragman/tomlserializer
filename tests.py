"""
Test suite!

"""
from os import path, getcwd, remove
import tomlstore

"""
Test the basic serializer by loading a dictionary, saving it as a file, then testing if you got the same thing back.

"""
test_dictionary = {"a": 0,
                   "b": 1}
tomlstore.store_object_as_toml(test_dictionary)
assert path.exists(f"{getcwd()}/objects/obj.toml")
saved_dictionary = tomlstore.toml_to_dict()
assert test_dictionary == saved_dictionary
remove(f"{getcwd()}/objects/obj.toml")