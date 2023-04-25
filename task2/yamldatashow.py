from yaml_loader import YAMLLoader

file_path = 'data.yaml'

yaml_loader = YAMLLoader(file_path)

data = yaml_loader.load_yaml()

if data is not None:
    print(data)
