from json_loader import JSONLoader

file_path = 'data.json'
json_loader = JSONLoader(file_path)
data = json_loader.load_json()
print(data)