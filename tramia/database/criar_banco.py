from tramia.database.conexao import conectar

# =============================================================================
# SCHEMA PROVISÓRIO — SUBSTITUIR PELO SCHEMA DO GABRIEL
#
# Este é o mesmo sistema modelado em Banco de Dados I. O schema definitivo
# segue a modelagem feita pelo Gabriel (autoria própria). Este bloco existe
# apenas para o código rodar enquanto isso, e contém só o que já foi decidido:
#   - Demanda e Responsável (um responsável tem várias demandas)
#   - responsavel_id aceita NULL (demanda nasce sem responsável)
#   - demanda tem prazo
# Status, datas e prioridade: decisões pendentes no pilar BD.
# =============================================================================
SCHEMA = """
CREATE TABLE IF NOT EXISTS responsavel (
    id    INTEGER PRIMARY KEY AUTOINCREMENT,
    nome  TEXT NOT NULL,
    email TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS demanda (
    id             INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo         TEXT NOT NULL,
    prazo          TEXT NOT NULL,
    status         TEXT NOT NULL,
    responsavel_id INTEGER,
    FOREIGN KEY (responsavel_id) REFERENCES responsavel (id)
);
"""


def criar_banco() -> None:
    """Cria as tabelas se ainda não existirem. Seguro para rodar a cada inicialização."""
    conexao = conectar()
    try:
        conexao.executescript(SCHEMA)
    finally:
        conexao.close()


if __name__ == "__main__":
    criar_banco()
    print("Banco criado.")
