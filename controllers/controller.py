from models.email_manager import EmailManager

class EmailController:
    def __init__(self, file_path=None):
        self.model = EmailManager(file_path)  # Passa o caminho da planilha para o EmailManager

    def load_file(self, file_path):
        """Carrega a planilha do Excel."""
        success, result = self.model.load_file(file_path)
        if success:
            return True, "Planilha carregada com sucesso!"
        else:
            return False, result  # Retorna a mensagem de erro
        
    def search_email(self, name):
        """Pesquisa e-mails e retorna uma lista de tuplas (email, senha)."""
        success, result = self.model.search_email(name)
        if success:
            return True, result  # Retorna a lista de tuplas (email, senha)
        else:
            return False, result  # Retorna a mensagem de erro

    def add_email_password(self, email, password):
        return self.model.add_email_password(email, password)

    def edit_email_password(self, email, new_email, new_password):
        return self.model.edit_email_password(email, new_email, new_password)

    def delete_email(self, email):
        return self.model.delete_email(email)

    def save_changes(self):
        return self.model.save_changes()