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

inserir_filmes("Avatar", "ação", 2009, 10)