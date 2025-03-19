from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

class AddScreen:
    def __init__(self, root, controller, back_callback):
        self.root = root
        self.controller = controller
        self.back_callback = back_callback

        # Frame principal
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Título
        self.label = ttk.Label(self.main_frame, text="Adicionar Novo Registro", font=("Arial", 18, "bold"))
        self.label.pack(pady=10)

        # Campos de entrada
        self.email_label = ttk.Label(self.main_frame, text="E-mail:")
        self.email_label.pack(pady=5)

        self.email_entry = ttk.Entry(self.main_frame, width=50)
        self.email_entry.pack(pady=5)

        self.password_label = ttk.Label(self.main_frame, text="Senha:")
        self.password_label.pack(pady=5)

        self.password_entry = ttk.Entry(self.main_frame, width=50)
        self.password_entry.pack(pady=5)

        # Botões
        self.buttons_frame = ttk.Frame(self.main_frame)
        self.buttons_frame.pack(pady=10)

        self.add_button = ttk.Button(self.buttons_frame, text="Adicionar", bootstyle=SUCCESS, command=self.add_email_password)
        self.add_button.pack(side="left", padx=5)

        self.back_button = ttk.Button(self.buttons_frame, text="Voltar", bootstyle=SECONDARY, command=self.back_callback)
        self.back_button.pack(side="left", padx=5)

    def add_email_password(self):
        """Adiciona um novo e-mail e senha."""
        email = self.email_entry.get().strip()
        password = self.password_entry.get().strip()
        
        success, message = self.controller.add_email_password(email, password)
        if success:
            messagebox.showinfo("Sucesso", message)
            self.email_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", message)