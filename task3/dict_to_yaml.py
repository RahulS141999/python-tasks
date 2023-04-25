import yaml

class YamlUtils:
    def write_to_file(data, file_path):
        with open(file_path, 'w') as file:
            yaml.dump(data,file)
        print(f"data written to the file")

    def read_from_file(file_path):
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
        return data