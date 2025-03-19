import ttkbootstrap as ttk
from views.list_screen import ListScreen
from views.add_screen import AddScreen
from controllers.controller import EmailController
import os

class MainApp:
    def __init__(self, root):
        self.root = root

        # Caminho da planilha no servidor de arquivos
        self.file_path = r"\\10.1.1.120\Callisto\Downloads\teste.xlsx"  # Caminho do arquivo

        # Inicializa o controlador e carrega a planilha automaticamente
        self.controller = EmailController(self.file_path)

        # Inicializa a tela de listagem
        self.show_list_screen()

    def show_list_screen(self):
        """Exibe a tela de listagem."""
        if hasattr(self, "add_screen"):
            self.add_screen.main_frame.destroy()

        self.list_screen = ListScreen(self.root, self.controller, self.show_add_screen)
        self.list_screen.main_frame.pack(fill="both", expand=True)

    def show_add_screen(self):
        """Exibe a tela de cadastro."""
        if hasattr(self, "list_screen"):
            self.list_screen.main_frame.destroy()

        self.add_screen = AddScreen(self.root, self.controller, self.show_list_screen)
        self.add_screen.main_frame.pack(fill="both", expand=True)

if __name__ == "__main__":
    root = ttk.Window(themename="cosmo")  # Escolha um tema
    app = MainApp(root)
    root.mainloop()