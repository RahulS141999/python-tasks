import yaml
import os


class YAMLLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_yaml(self):
        try:
             file_path = os.path.join(os.path.dirname(__file__), self.file_path)
             with open(file_path, 'r') as file:
                 data = yaml.safe_load(file)
                 return data
        except FileNotFoundError:
            print(f"Error: File not found")
            return None