import requests
import streamlit as st
import pandas as pd
import time
API_URL = "http://127.0.0.1:8000/"
st.set_page_config(page_title="Gerenciador de Filmes", page_icon="🎬")

st.title("🎥 Gerenciador de Filmes")

menu = st.sidebar.radio("Navegção", ["Catálogo", "Adicionar Filme"])

if menu == "Catálogo": 
    st.subheader("Catálogo de Filmes")
    response = requests.get(f"{API_URL}/filmes")
    if response.status_code == 200:
        filmes = response.json().get("Filmes", [])
        if filmes:
            st.dataframe(filmes)
        else:
            st.warning("Nenhum livro encontrado!")      
    else:
        st.error("Erro ao acessar a API")

elif menu == "Adicionar Filme":
    titulo = st.text_input("Digite o nome do titulo do filme")
    genero = st.text_input("Digite o genero do filme")
    ano = st.number_input("Digite o ano de lançamento", min_value=1880,max_value= 2100, step=1)
    avaliacao = st.number_input("Digite a avaliação", min_value=0.0, max_value=10.0, step=0.1)
    if titulo:
        if genero:
            if st.button("Adicionar"):
                dados = {"titulo" : titulo, "genero" : genero, "ano" : ano, "avaliacao" : avaliacao}
                response = requests.post(f"{API_URL}/filmes", params=dados)
                if response.status_code == 200:
                    st.success("Livro adicionado com sucesso!")
                    time.sleep(2)
                    st.rerun()
                else:
                    st.error("erro ao adicionar o livro")
        else:
            st.warning("insira o genero do filme")
    else:
            st.warning("insira o titulo do filme")