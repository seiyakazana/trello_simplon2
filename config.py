import json

DATA_FILE = "src/data.json"

with open(DATA_FILE, "r") as f:
    data = json.load(f)


def write_data(data):
    with open(DATA_FILE, "w", encoding='utf-8') as f:
        write = json.dump(f, data)

         