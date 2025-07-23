# app.py
# Este arquivo cuida APENAS da interface com o usuário usando Streamlit.

import streamlit as st
# Importando nossas funções do outro arquivo
from assistente_mestre import config_model, gerar_background_cidade

# --- CONSTRUÇÃO DA INTERFACE STREAMLIT ---

st.set_page_config(page_title="Forja de Mundos RPG", page_icon="🧙‍♂️")
st.title("🧙‍♂️ Forja de Mundos")
st.subheader("Seu assistente para criar cidades de RPG inesquecíveis")

# --- BARRA LATERAL (SIDEBAR) PARA ENTRADAS ---

st.sidebar.header("Parâmetros da Cidade")

# Widgets de entrada
nome_cidade = st.sidebar.text_input("Nome da Cidade", placeholder="Ex: Lançatroz, Porto Nebuloso")
sistema_rpg = st.sidebar.selectbox(
    "Sistema de RPG",
    ["D&D 5e", "Tormenta20", "Pathfinder 2e", "Vampiro: A Máscara", "Chamado de Cthulhu", "Outro"]
)
localizacao_geral = st.sidebar.text_input("Localização no Mundo", placeholder="Ex: No coração de uma floresta amaldiçoada")
vibe_principal = st.sidebar.text_input("Vibe Principal da Cidade", placeholder="Ex: Cidade portuária de piratas")
elemento_unico = st.sidebar.text_area("Elemento Único e Intrigante", placeholder="Ex: Toda a magia é extraída de um golem adormecido...")

# Botão para iniciar a geração
if st.sidebar.button("Forjar Cenário!"):
    if not all([nome_cidade, sistema_rpg, localizacao_geral, vibe_principal, elemento_unico]):
        st.error("Mestre, por favor, preencha todos os campos para forjar sua cidade!")
    else:
        # 1. Chama a função de configuração do outro módulo
        modelo_gemini = config_model() 
        
        if modelo_gemini:
            with st.spinner(f"Os arquitetos astrais estão construindo {nome_cidade}... Um momento..."):
                # 2. Chama a função de geração do outro módulo
                background_gerado = gerar_background_cidade(
                    model=modelo_gemini,
                    nome_cidade=nome_cidade,
                    localizacao_geral = localizacao_geral,
                    sistema_rpg=sistema_rpg,
                    vibe_principal=vibe_principal,
                    elemento_unico=elemento_unico
                )
                
                st.subheader(f"Pergaminho de: {nome_cidade}")
                st.markdown(background_gerado)
                st.download_button(
                    label="Baixar Pergaminho (.md)",
                    data=background_gerado,
                    file_name=f"{nome_cidade.lower().replace(' ', '_')}.md",
                    mime="text/markdown"
                )
        else:
            st.error("Houve uma falha na conexão com os planos superiores (erro na API).")
else:
    st.info("Preencha os detalhes da sua cidade na barra lateral e clique em 'Forjar Cenário!' para começar sua aventura.")