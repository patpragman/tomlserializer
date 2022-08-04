"""
Test suite!

"""
from os import path, getcwd, remove, listdir
import tomlstore
from server import TomlServer
from pprint import pprint
from random import randrange

from datetime import datetime, timedelta
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

# now a speed test - let's read and write millions of objects and see how long it takes

start_time = datetime.utcnow()
speed_test_server = TomlServer()

template = {"index": None,
            "name": None,
            "value": None}

for i in range(0, 1_000_000):
    obj = template.copy()
    obj["index"] = i
    obj["name"] = str(i)
    obj["value"] = "".join([chr(randrange(65, 126, 1)) for j in range(0, 512)])
    speed_test_server.store(obj, obj['name'])
    del obj

del speed_test_server
speed_test_server = TomlServer()
store_time = datetime.utcnow()
time_to_store_all = (store_time - start_time).seconds

for i in range(0, 1_000_000):
    obj = speed_test_server.retrieve(str(i))
    obj['value'] = f"hello_{i}"
    speed_test_server.store(obj['name'])
    speed_test_server.remove(str(i))
    del obj

delete_time = datetime.utcnow()
total_delete_time = (delete_time - store_time).seconds
total_time = (delete_time - start_time).seconds

print("Time stats:")
print("time to store all:", time_to_store_all, "s")
print("time to retrieve, edit, restore, then delete all all", total_delete_time, "s")
print("time for whole thing", total_time, "s")
