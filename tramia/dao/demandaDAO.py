from tramia.database.conexao import conectar
from tramia.models.demanda import Demanda
from datetime import date

class DemandaDAO:
    def inserir(self, demanda: Demanda) -> None:
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                INSERT INTO demanda (titulo, prazo, responsavel_id, status)
                VALUES (?, ?, ?, ?)
                """,
                (demanda.titulo, demanda.prazo, demanda.responsavel_id , demanda.status),
            )
        finally:
            conexao.close()
        pass

    def atualizarStatus(self, demanda, prazo, id):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                UPADATE Demanda
                SET status = ?
                WHERE id = ? 
                VALUES (?, ?)
                """,
                (demanda.prazo, demanda.id),
        )
        finally:
            conexao.close()
        
        pass

    def deletar(self, id):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                DELETE FROM Demanda WHERE id = ?
                """,
                (id,)
            )
        finally:
            conexao.close()
        pass

    def buscar_id(self, id):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
                """
                SELECT FROM Demanda WHERE id = ?
                """,
                (id,),
            )
            linha = cursor.fetchone()
        finally:
            conexao.close()
        return self._para_objeto(linha) if linha else None

        pass

    def listarDemandas(self, id):
        conexao = conectar()
        try:
            cursor = conexao.cursor()
            cursor.execute(
            """
            SELECT id, titulo, prazo, responsavel_id WHERE id = ?
            """,
            (id,),  
            )
            linha = cursor.fetchall()
        finally:
            conexao.close()
        return self._para_objeto(linha) if linha else None
        pass



    @staticmethod
    def _para_objeto(linha):
        return Demanda(id=linha["id"], titulo=linha["titulo"], prazo=linha["prazo"], responsavel_id=linha["responsavel"], status=linha["status"])
