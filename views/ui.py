import tkinter as tk
from tkinter import messagebox, filedialog
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class EmailPasswordGUI:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Gerenciador de E-mails e Senhas")
        self.root.geometry("600x400")

        # Interface
        self.label = ttk.Label(root, text="Gerenciador de E-mails e Senhas", font=("Arial", 16))
        self.label.pack(pady=20)

        self.load_button = ttk.Button(root, text="Carregar Planilha", bootstyle=SUCCESS, command=self.load_file)
        self.load_button.pack(pady=10)

        self.search_label = ttk.Label(root, text="Pesquisar E-mail:")
        self.search_label.pack(pady=5)

        self.search_entry = ttk.Entry(root, width=40)
        self.search_entry.pack(pady=5)

        self.search_button = ttk.Button(root, text="Pesquisar", bootstyle=INFO, command=self.search_email)
        self.search_button.pack(pady=5)

        self.result_label = ttk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        # Botões para editar, excluir e copiar
        self.copy_button = ttk.Button(root, text="Copiar Senha", bootstyle=SUCCESS, command=self.copy_password)
        self.copy_button.pack(pady=5)

        self.edit_button = ttk.Button(root, text="Editar", bootstyle=WARNING, command=self.show_edit_screen)
        self.edit_button.pack(pady=5)

        self.delete_button = ttk.Button(root, text="Excluir", bootstyle=DANGER, command=self.delete_email)
        self.delete_button.pack(pady=5)

    def load_file(self):
        """Carrega a planilha do Excel."""
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx *.xls")])
        if file_path:
            success, message = self.controller.load_file(file_path)
            if success:
                messagebox.showinfo("Sucesso", message)
            else:
                messagebox.showerror("Erro", message)

    def search_email(self):
        """Pesquisa um e-mail e retorna a senha."""
        email = self.search_entry.get().strip()
        if not email:
            messagebox.showwarning("Aviso", "Digite um e-mail para pesquisar.")
            return

        success, result = self.controller.search_email(email)
        if success:
            self.result_label.config(text=f"Senha: {result}")
        else:
            self.result_label.config(text=result)

    def copy_password(self):
        """Copia a senha para a área de transferência."""
        password = self.result_label.cget("text").replace("Senha: ", "")
        if password and password != "E-mail não encontrado.":
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            messagebox.showinfo("Sucesso", "Senha copiada para a área de transferência!")
        else:
            messagebox.showwarning("Aviso", "Nada para copiar.")

    def show_edit_screen(self):
        """Exibe a tela de edição de e-mail e senha."""
        # Implemente a tela de edição aqui
        pass

    def delete_email(self):
        """Exclui um e-mail."""
        email = self.search_entry.get().strip()
        if not email:
            messagebox.showwarning("Aviso", "Digite um e-mail para excluir.")
            return

        success, message = self.controller.delete_email(email)
        if success:
            messagebox.showinfo("Sucesso", message)
        else:
            messagebox.showwarning("Aviso", message)