import json
from pathlib import Path


class Indices:
    #Construtor da classe Indices, que carrega os índices do arquivo JSON se ele existir
    def __init__(self):
        if Path("Collections/indices.json").exists():
            with open("Collections/indices.json", "r") as file:
                self.indices = json.load(file)
        else:
            print("Arquivo indices.json não encontrados.")

    #Método para obter os índices carregados
    def get_indices(self):
        return self.indices

    #Método para salvar os índices no arquivo JSON
    def save_indices(self):
        with open("Collections/indices.json", "w", encoding="utf-8") as new_file:
            json.dump(self.indices, new_file, ensure_ascii=False, indent=4)