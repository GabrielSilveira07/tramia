from tramia.database.conexao import conectar
from tramia.models.responsavel import Responsavel


class ResponsavelDAO:
    def inserir(self, responsavel):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                INSERT INTO responsavel (nome, email)
                VALUES (?, ?)
                """,
                (responsavel.nome, responsavel.email),
            )
            conexao.commit()
            responsavel.id = cursor.lastrowid
        finally:
            conexao.close()

    def listar(self):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("SELECT id, nome, email FROM responsavel")
            linhas = cursor.fetchall()
        finally:
            conexao.close()
        return [self._para_objeto(linha) for linha in linhas]

    def buscarID(self, id):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                "SELECT id, nome, email FROM responsavel WHERE id = ?",
                (id,),
            )
            linha = cursor.fetchone()
        finally:
            conexao.close()
        return self._para_objeto(linha) if linha else None

    def deletar(self, id):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute("DELETE FROM responsavel WHERE id = ?", (id,))
            conexao.commit()
        finally:
            conexao.close()

    @staticmethod
    def _para_objeto(linha):
        return Responsavel(id=linha["id"], nome=linha["nome"], email=linha["email"])