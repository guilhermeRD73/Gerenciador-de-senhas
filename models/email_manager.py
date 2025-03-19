import pandas as pd
from tkinter import filedialog
import os
import sys

class EmailManager:
    def __init__(self, file_path=None):
        self.file_path = file_path  # Armazena o caminho da planilha
        self.data = pd.DataFrame(columns=["Email", "Senha"])
        if file_path and os.path.exists(file_path):  # Verifica se o arquivo existe
            self.load_file(file_path)
        
    def load_file(self, file_path):
        """Carrega a planilha do Excel."""
        try:
            self.data = pd.read_excel(file_path)
            return True, "Planilha carregada com sucesso!"
        except Exception as e:
            return False, f"Erro ao carregar a planilha: {e}"

    def search_email(self, name):
        """Pesquisa e-mails por nome."""
        try:
            results = self.data[self.data["Email"].str.contains(name, case=False)]
            if not results.empty:
                return True, list(zip(results["Email"], results["Senha"]))
            else:
                return False, "Nenhum e-mail encontrado."
        except Exception as e:
            return False, f"Erro ao pesquisar: {e}"

    def add_email_password(self, email, password):
        """Adiciona um novo e-mail e senha."""
        if email in self.data["Email"].values:
            return False, "E-mail já existe."
        
        # Adiciona o novo registro ao DataFrame
        self.data = self.data._append({"Email": email, "Senha": password}, ignore_index=True)
        
        # Salva as alterações na planilha
        success, message = self.save_changes()
        if success:
            return True, "E-mail adicionado com sucesso!"
        else:
            return False, message

    def edit_email_password(self, email, new_email, new_password):
        """Edita um e-mail e senha existente."""
        if email not in self.data["Email"].values:
            return False, "E-mail não encontrado."
        
        # Atualiza o e-mail e a senha
        self.data.loc[self.data["Email"] == email, ["Email", "Senha"]] = [new_email, new_password]
        
        # Salva as alterações na planilha
        success, message = self.save_changes()
        if success:
            return True, "E-mail atualizado com sucesso!"
        else:
            return False, message

    def delete_email(self, email):
        """Exclui um e-mail."""
        if email not in self.data["Email"].values:
            return False, "E-mail não encontrado."
        
        # Remove o e-mail do DataFrame
        self.data = self.data[self.data["Email"] != email]
        
        # Salva as alterações na planilha
        success, message = self.save_changes()
        if success:
            return True, "E-mail excluído com sucesso!"
        else:
            return False, message

    def save_changes(self):
        """Salva as alterações no arquivo Excel."""
        try:
            self.data.to_excel(self.file_path, index=False)
            return True, "Alterações salvas com sucesso!"
        except Exception as e:
            return False, f"Erro ao salvar: {e}"