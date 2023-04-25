from dict_to_yaml import YamlUtils

data = {'name': 'sachin', 'age': 38, 'city': 'mumbai'}

YamlUtils.write_to_file(data, 'data.yaml')

loaded_data = YamlUtils.read_from_file('data.yaml')
print(loaded_data)
