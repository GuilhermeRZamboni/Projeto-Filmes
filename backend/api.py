from fastapi import FastAPI
import funcao

app = FastAPI(title="Gerenciador de Filmes")

#Rodar o codigo:
#cd backend
# python -m uvicorn api:app --reload
@app.get("/filmes")
def listar_filmes():
    filmes = funcao.listar_filmes()
    lista = []
    for filme in filmes:
        lista.append({"ID" : filme[0], "Titulo" : filme[1], "Genero" : filme[2], "Ano" : filme[3], "Avaliação" : filme[4] } )
    return {"Filmes" : lista}
@app.get("/")
def home():
    return {"mensagem" : "Bem-vindo ao gerenciador de filmes"}

@app.post("/filmes")
def criar_filmes(titulo: str, genero: str, ano:int, avaliacao:float):
    funcao.inserir_filmes(titulo, genero, ano, avaliacao)
    return {"mensagem" : "Filme adicionado com sucesso"}

@app.delete("/filmes")
def deletar_filme (id:int):
    funcao.deletar_filme(id)
    return {"Mensagem" : "Filme deletado com sucesso"}
