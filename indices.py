import json
from pathlib import Path


class Indices:
    def __init__(self):
        if Path("Collections/indices.json").exists():
            with open("Collections/indices.json", "r") as file:
                self.indices = json.load(file)
        else:
            print("Arquivo indices.json não encontrados.")

    def get_indices(self):
        return self.indices

    def save_indices(self):
        with open("Collections/indices.json", "w", encoding="utf-8") as new_file:
            json.dump(self.indices, new_file, ensure_ascii=False, indent=4)