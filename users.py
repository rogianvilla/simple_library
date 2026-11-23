import json
from pathlib import Path


class Users:
    #Método construtor da classe Users, que verifica se o arqui vo JSON de usuários existe. Se existir, carrega os usuários do arquivo; caso contrário, inicializa uma lista vazia.
    def __init__(self):
        if Path("Collections/users.json").exists():
            with open("Collections/users.json", "r") as file:
                self.users = json.load(file)
        else:
            self.users = []

    #Método para salvar os usuários no arquivo JSON ao encerrar o programa.
    def save_users(self):
        with open("Collections/users.json", "w", encoding="utf-8") as new_file:
            json.dump(self.users, new_file, ensure_ascii=False, indent=4)

    #Metodo para adicionar um usuário à lista de usuários. Recebe os parâmetros do usuário, cria um dicionário representando o usuário e adiciona à lista de usuários.
    def add_user(self, name, email, cpf):
        user = {
            "name": name,
            "email": email,
            "cpf": cpf
        }
        self.users.append(user)

    #Método para verificar se um usuário já está cadastrado com base no CPF fornecido. Retorna True se o usuário existir, caso contrário, retorna False.
    def verify_user(self, cpf):
        for user in self.users:
            if user['cpf'] == cpf:
                return True
        return False

    #Método para obter as informações de um usuário com base no CPF fornecido. Retorna o dicionário do usuário se encontrado, caso contrário, retorna None.
    @staticmethod
    def get_user(self, cpf):
        for user in self.users:
            if user['cpf'] == cpf:
                return user
        return None

    #Metodo para listar todos os usuários cadastrados. Exibe o nome, email e CPF de cada usuário.
    def list_all_users(self):
        print("\n--- Lista de Usuários ---")
        if not self.users:
            print("Nenhum usuário cadastrado.")
            return
        else:
            for user in self.users:
                print(f"Nome: {user['name']}, Email: {user['email']}, CPF: {user['cpf']}")

    #Método para atualizar as informações de um usuário com base no CPF fornecido.
    def update_user(self, cpf, new_name, new_email):
        for user in self.users:
            if user['cpf'] == cpf:
                user['name'] = new_name
                user['email'] = new_email
                print(f"Usuário com CPF {cpf} atualizado com sucesso.")
                return
        print(f"Usuário com CPF {cpf} não encontrado.")
        return

    #Método para remover um usuário da lista de usuários com base no CPF fornecido.
    def remove_user(self, cpf):
        for user in self.users:
            if user['cpf'] == cpf:
                self.users.remove(user)
                print(f"Usuário com CPF {cpf} removido com sucesso.")
                return
        print(f"Usuário com CPF {cpf} não encontrado.")
        return


    @staticmethod
    def cpf_validate(cpf):
        # Remove pontos e traços
        cpf = ''.join(filter(str.isdigit, cpf))

        # Deve ter 11 dígitos
        if len(cpf) != 11:
            return False

        # Evita CPFs com todos os números iguais
        if cpf == cpf[0] * 11:
            return False

        # Primeiro dígito verificador
        soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
        resto = (soma * 10) % 11
        digito1 = 0 if resto == 10 else resto

        if digito1 != int(cpf[9]):
            return False

        # Segundo dígito verificador
        soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
        resto = (soma * 10) % 11
        digito2 = 0 if resto == 10 else resto

        if digito2 != int(cpf[10]):
            return False

        return True