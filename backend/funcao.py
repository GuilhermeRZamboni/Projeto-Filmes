from conexao import conectar

def criar_tabela():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute("""CREATE TABLE IF NOT EXISTS filmes (
                           id SERIAL PRIMARY KEY,
                           titulo TEXT NOT NULL,
                           genero TEXT NOT NULL,
                           ano INTEGER NOT NULL,
                           avaliacao REAL)""")
            conexao.commit()

        except Exception as erro:
            print(f"Erro ao criar tabela: {erro}")
        finally:
            cursor.close()
            conexao.close()

# criar_tabela()


def inserir_filmes(titulo, genero, ano, avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO filmes (titulo, genero, ano, avaliacao) VALUES (%s, %s, %s, %s)",
                (titulo, genero, ano, avaliacao)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao inserir filme: {erro}")
        finally:
            cursor.close()
            conexao.close()



def listar_filmes():
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                    "SELECT * FROM filmes ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao inserir filme: {erro}")
        finally:
            cursor.close()
            conexao.close()

filmes = listar_filmes()
for linha in filmes:
    print(f"Titulo - {linha[1]}, Genero - {linha[2]}, Ano - {linha[3]}, Avaliação - {linha[4]}")

def atualizar_filme(id, nova_avaliacao):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "UPDATE filmes SET avaliacao = %s WHERE id = %s",
                (nova_avaliacao, id))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar filmes, {erro}")
        finally:
            conexao.close()
            cursor.close()

# atualizar_filme(2, 9)
# listar_filmes()


def deletar_filme(id):
    conexao, cursor = conectar()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM filmes WHERE id = %s",
                (id,))
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao deletar filmes, {erro}")
        finally:
            conexao.close()
            cursor.close()
# deletar_filme(2)