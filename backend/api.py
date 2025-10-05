from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de Filmes")

@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filmes()
    lista = []  
    lista.append({"ID" : filme[0], "Titulo" : filme[1], "Genero" : filme[2], "Ano" : filme[3], "Avaliação" : filme[4] } for filme in filmes)
    return {"Filmes" : lista}
@app.get("/")
def home():
    return {"mensagem" : "Quero Café"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano:int, avaliacao:float):
    funcao.inserir_filmes(titulo, genero, ano, avaliacao)
    return {"mensagem" : "Filme adicionado com sucesso"}

