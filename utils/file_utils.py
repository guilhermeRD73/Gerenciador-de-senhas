import pandas as pd

def load_excel(file_path):
    """
    Carrega uma planilha Excel e retorna um DataFrame.
    
    Args:
        file_path (str): Caminho do arquivo Excel.
    
    Returns:
        tuple: (success, data)
            - success (bool): True se o arquivo foi carregado com sucesso.
            - data (pd.DataFrame or str): DataFrame com os dados ou mensagem de erro.
    """
    try:
        df = pd.read_excel(file_path)
        return True, df
    except Exception as e:
        return False, f"Erro ao carregar a planilha: {e}"

def save_excel(df, file_path):
    """
    Salva um DataFrame em um arquivo Excel.
    
    Args:
        df (pd.DataFrame): DataFrame a ser salvo.
        file_path (str): Caminho do arquivo Excel.
    
    Returns:
        tuple: (success, message)
            - success (bool): True se o arquivo foi salvo com sucesso.
            - message (str): Mensagem de sucesso ou erro.
    """
    try:
        df.to_excel(file_path, index=False)
        return True, "Planilha salva com sucesso!"
    except Exception as e:
        return False, f"Erro ao salvar a planilha: {e}"