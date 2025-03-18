import pandas as pd
from tkinter import filedialog, messagebox

class EmailManager:
    def __init__(self):
        self.data = pd.DataFrame(columns=["Email", "Senha"])

    def load_file(self, file_path):
        """Carrega uma planilha Excel."""
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
        self.data = self.data.append({"Email": email, "Senha": password}, ignore_index=True)
        return True, "E-mail adicionado com sucesso!"

    def edit_email_password(self, email, new_email, new_password):
        """Edita um e-mail e senha existente."""
        if email not in self.data["Email"].values:
            return False, "E-mail não encontrado."
        self.data.loc[self.data["Email"] == email, ["Email", "Senha"]] = [new_email, new_password]
        return True, "E-mail atualizado com sucesso!"

    def delete_email(self, email):
        """Exclui um e-mail."""
        if email not in self.data["Email"].values:
            return False, "E-mail não encontrado."
        self.data = self.data[self.data["Email"] != email]
        return True, "E-mail excluído com sucesso!"

    def save_changes(self):
        """Salva as alterações no arquivo Excel."""
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
            if file_path:
                self.data.to_excel(file_path, index=False)
                return True, "Alterações salvas com sucesso!"
            else:
                return False, "Nenhum arquivo selecionado."
        except Exception as e:
            return False, f"Erro ao salvar: {e}"