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