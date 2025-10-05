import requests
import streamlit as st
import pandas as pd

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
            product_data = {
            "Titulo": [filme['Titulo'] for filme in filmes[0]],
            "Genero": [filme['Genero'] for filme in filmes[0]],
            "Ano": [filme['Ano'] for filme in filmes[0]],
            "Avaliação ": [filme ['Avaliação'] for filme in filmes[0]],
            
        }
            st.table(product_data, border="horizontal")    
        else:
            st.warning("Nenhum livro encontrado!")      
    else:
        st.error("Erro ao acessar a API")