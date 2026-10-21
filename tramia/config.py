from pathlib import Path

# Caminho absoluto: o banco é encontrado de qualquer diretório onde o programa rodar
# (corrige o caminho relativo da StarterBox).
RAIZ_PROJETO = Path(__file__).resolve().parent.parent
CAMINHO_BANCO = RAIZ_PROJETO / "dados" / "tramia.db"
