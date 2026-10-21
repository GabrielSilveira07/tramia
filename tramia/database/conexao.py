import sqlite3

from tramia.config import CAMINHO_BANCO


def conectar() -> sqlite3.Connection:
    """Abre uma conexão com o banco. Ponto único de acesso: os DAOs só usam esta função."""
    CAMINHO_BANCO.parent.mkdir(parents=True, exist_ok=True)
    conexao = sqlite3.connect(CAMINHO_BANCO)
    conexao.row_factory = sqlite3.Row  # linhas acessíveis por nome de coluna (linha["titulo"])
    conexao.execute("PRAGMA foreign_keys = ON")  # o SQLite só valida FK com isso ligado
    return conexao
