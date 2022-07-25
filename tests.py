"""
Test suite!

"""
from os import path, getcwd, remove, listdir
import tomlstore
from server import TomlServer
from pprint import pprint
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


test_server = TomlServer()
test_dictionary['c'] = 'hello world!'
test_dictionary['d'] = 1.0005 * 10**2
test_server.store(test_dictionary, "test")
assert path.exists(f"{getcwd()}/objects/test")
test_dictionary_2 = test_server.retrieve("test")
assert test_dictionary == test_dictionary_2
test_server.remove("test")
assert not path.exists(f"{getcwd()}/objects/test")
meta_data_path = test_server.metadata_path
del test_server
assert path.exists(meta_data_path)
remove(meta_data_path)

# big nested dictionary test
big_dict_energy = {
    str(i): i for i in range(0, 100_000)
}

big_dict_energy['nested'] = {str(j): j for j in range(100_000, 200_000)}
#  pprint(big_dict_energy)  # debug
server = TomlServer()
server.store(big_dict_energy, "bde")
# we visually inspected the file here
assert path.exists(f"{getcwd()}/objects/bde")
remove(f"{getcwd()}/objects/bde")
del big_dict_energy
bde_meta_path = server.metadata_path
del server
remove(bde_meta_path)
assert not listdir(f"{getcwd()}/objects")