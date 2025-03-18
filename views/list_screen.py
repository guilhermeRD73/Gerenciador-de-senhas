from tkinter import filedialog, messagebox
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class ListScreen:
    def __init__(self, root, controller, open_add_screen_callback):
        self.root = root
        self.controller = controller
        self.open_add_screen_callback = open_add_screen_callback

        # Frame principal
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        self.label = ttk.Label(self.main_frame, text="Listagem de E-mails e Senhas", font=("Arial", 18, "bold"))
        self.label.pack(pady=10)

        # Botão para carregar planilha
        self.load_button = ttk.Button(self.main_frame, text="Carregar Planilha", bootstyle=SUCCESS, command=self.load_file)
        self.load_button.pack(pady=10)

        # Frame de pesquisa
        self.search_frame = ttk.LabelFrame(self.main_frame, text="Pesquisar E-mail", padding=10)
        self.search_frame.pack(fill="x", pady=10)

        self.search_entry = ttk.Entry(self.search_frame, width=50)
        self.search_entry.pack(side="left", padx=5)

        self.search_button = ttk.Button(self.search_frame, text="Pesquisar", bootstyle=INFO, command=self.search_email)
        self.search_button.pack(side="left", padx=5)

        # Frame de resultados
        self.result_frame = ttk.LabelFrame(self.main_frame, text="Resultados", padding=10)
        self.result_frame.pack(fill="both", expand=True, pady=10)

        self.result_listbox = tk.Listbox(self.result_frame, width=80, height=10)
        self.result_listbox.pack(fill="both", expand=True, padx=5, pady=5)

        # Botões para editar e excluir
        self.buttons_frame = ttk.Frame(self.result_frame)
        self.buttons_frame.pack(pady=10)

        self.edit_button = ttk.Button(self.buttons_frame, text="Editar", bootstyle=WARNING, command=self.edit_email)
        self.edit_button.pack(side="left", padx=5)

        self.delete_button = ttk.Button(self.buttons_frame, text="Excluir", bootstyle=DANGER, command=self.delete_email)
        self.delete_button.pack(side="left", padx=5)

        # Botão para adicionar novo registro
        self.add_button = ttk.Button(self.main_frame, text="Adicionar Novo Registro", bootstyle=PRIMARY, command=self.open_add_screen_callback)
        self.add_button.pack(pady=10)

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
        """Pesquisa e-mails e exibe os resultados."""
        name = self.search_entry.get().strip()
        if not name:
            messagebox.showwarning("Aviso", "Digite um nome para pesquisar.")
            return

        success, result = self.controller.search_email(name)
        if success:
            self.result_listbox.delete(0, tk.END)
            for email, senha in result:
                self.result_listbox.insert(tk.END, f"E-mail: {email} | Senha: {senha}")
        else:
            self.result_listbox.delete(0, tk.END)
            self.result_listbox.insert(tk.END, result)

    def edit_email(self):
        """Edita o e-mail selecionado."""
        selected = self.result_listbox.curselection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um e-mail para editar.")
            return

        selected_text = self.result_listbox.get(selected)
        email = selected_text.split(" | ")[0].replace("E-mail: ", "")
        senha = selected_text.split(" | ")[1].replace("Senha: ", "")

        # Abre a janela de edição
        self.edit_window = ttk.Toplevel(self.root)
        self.edit_window.title("Editar E-mail e Senha")
        self.edit_window.geometry("400x200")

        # Frame de edição
        edit_frame = ttk.Frame(self.edit_window, padding=20)
        edit_frame.pack(fill="both", expand=True)

        # Campo para editar o e-mail
        ttk.Label(edit_frame, text="E-mail:").pack(pady=5)
        self.edit_email_entry = ttk.Entry(edit_frame, width=40)
        self.edit_email_entry.pack(pady=5)
        self.edit_email_entry.insert(0, email)

        # Campo para editar a senha
        ttk.Label(edit_frame, text="Senha:").pack(pady=5)
        self.edit_password_entry = ttk.Entry(edit_frame, width=40)
        self.edit_password_entry.pack(pady=5)
        self.edit_password_entry.insert(0, senha)

        # Botão para salvar as alterações
        ttk.Button(edit_frame, text="Salvar", bootstyle=SUCCESS, command=lambda: self.save_edit(email)).pack(pady=10)

    def save_edit(self, old_email):
        """Salva as alterações feitas na edição."""
        new_email = self.edit_email_entry.get().strip()
        new_password = self.edit_password_entry.get().strip()

        if not new_email or not new_password:
            messagebox.showwarning("Aviso", "Preencha o e-mail e a senha.")
            return

        success, message = self.controller.edit_email_password(old_email, new_email, new_password)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.edit_window.destroy()
            self.search_email()
        else:
            messagebox.showwarning("Aviso", message)

    def delete_email(self):
        """Exclui o e-mail selecionado."""
        selected = self.result_listbox.curselection()
        if not selected:
            messagebox.showwarning("Aviso", "Selecione um e-mail para excluir.")
            return

        email = self.result_listbox.get(selected).split(" | ")[0].replace("E-mail: ", "")
        success, message = self.controller.delete_email(email)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.search_email()
        else:
            messagebox.showwarning("Aviso", message)