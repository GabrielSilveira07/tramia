import database.conexao from conectar  

class ResponsavelDAO:   #cria classe
    def inserir(self, responsavel): #função de inserir obejto "funcionario"responsavel
        conexao = conectar()

        cursor = conexao.cursor()   #objeto responsável por executar a função

        cursor.execute( #insere na tabela USUARIO os valores coletados com os gets
            """
            INSERT INTO responsavel(nome, email)
            VALUES(?,?)
            """,
            (
                responsavel.getNome(),
                responsavel.getEmail()
            )
        )

        conexao.commit()    #confirma as operações e transação no banco de dados
        conexao.close() #finaliza conexao

    def listar(self, usuario):
        conexao = conectar()

        cursor = conexao.cursor()

        cursor.execute( #seleciona os nomes dos responsáveis
            """
            SELECT nome FROM responsavel    
            """,
            (
                responsaveis = cursor.fetchall()    #busca todos os nomes selecionados
            )
        )

        conexao.close()

    def buscarID(self, id):
        conexao = conectar()

        cursor = conexao.cursor()

        cursor.execute( #seleciona todos os funcionarios, enquanto o id seja igual ao informado
            """
            SELECT * FROM responsavel
            WHERE id = ?
            """,
            (id,)
        )
        
        responsavel = cursor.fetchone() #coleta o dado

        cursor.close()
        conexao.close()
        
        return responsavel  #devolve id pro responsavel

    def deletar(self, id):
        conexao = conectar()

        cursor = conexao.cursor()

        cursor.execute(
            """
            DELETE FROM responsavel
            WHERE id = ?
            """,
            (id, )
        )

        conexao.commit()
        cursor.close()
        conexao.close()