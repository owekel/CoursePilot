import json
from pathlib import Path

def save_practice_set(practice_set, file_path):
    
    path = Path(file_path)

    path.parent.mkdir(parents=True, exist_ok=True)

    
    # 1. Open the file in write mode
    # 2. Use json.dump() to save practice_set
    with open(file_path, "w") as file:
        json.dump(practice_set, file, indent = 4)

def load_practice_set(file_path):
    # 1. Open the JSON file in read mode
    # 2. Convert the JSON into a Python dictionary

    with open(file_path, "r") as file:
        practice_set = json.load(file)

    # 3. Return the dictionary

    return practice_set

def list_practice_sets():
    folder = Path("data/practice_sets")

    # 1. Find every JSON file using .glob()
    files = list(folder.glob("*.json"))
    # 2. Sort the files alphabetically
    files = sorted(files)

    return files