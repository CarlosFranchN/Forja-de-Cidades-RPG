import streamlit as st
from assistente_mestre import config_model, gerar_background_cidade

# --- CONSTRUÇÃO DA INTERFACE STREAMLIT ---

st.set_page_config(
    page_title="Forja de Mundos RPG", 
    page_icon="🏰", 
    layout="wide" 
)
st.title("🧙‍♂️ Forja de Mundos")
st.subheader("Seu assistente para criar cidades de RPG inesquecíveis")

# Estilos customizado
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
    }
    .big-font {
        font-size:20px !important;
    }
</style>
""", unsafe_allow_html=True)


# GERENCIAMENTO DE ESTADO (MEMÓRIA) ---
# Isso impede que o texto suma se o usuário interagir com a tela
if 'ultimo_resultado' not in st.session_state:
    st.session_state['ultimo_resultado'] = None
if 'nome_cidade_atual' not in st.session_state:
    st.session_state['nome_cidade_atual'] = ""


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
    

st.title("🧙‍♂️ Forja de Mundos")
st.markdown("---")


if st.session_state['ultimo_resultado']:
    
    col_texto, col_download = st.columns([4, 1])
    
    with col_texto:
        st.subheader(f"📜 Pergaminho: {st.session_state['nome_cidade_atual']}")
    
    with col_download:
        st.download_button(
            label="📥 Baixar Markdown",
            data=st.session_state['ultimo_resultado'],
            file_name=f"{st.session_state['nome_cidade_atual'].lower().replace(' ', '_')}.md",
            mime="text/markdown"
        )
    
    
    with st.container(border=True):
        st.markdown(st.session_state['ultimo_resultado'])


else:
    col1, col2 = st.columns(2)
    with col1:
        st.info("👈 **Comece pela esquerda!**\n\nPreencha os dados na barra lateral para gerar sua primeira cidade.")
        st.markdown("""
        ### O que esta ferramenta cria?
        - 🏙️ **Descrição Sensorial** imersiva
        - 📜 **Lore e História** profunda
        - ⚖️ **Governo e Facções** políticas
        - 📍 **Locais (NPCs)** prontos para usar
        - ⚔️ **Ganchos de Aventura** mecânicos
        """)
    
    with col2:
        
        st.markdown("### Exemplo de Criação:")
        st.code("""
        Cidade: Porto de Ferro
        Sistema: D&D 5e
        Vibe: Industrial e Mágica
        
        > "Porto de Ferro cheira a óleo de máquina e ozônio arcano. 
        As ruas são iluminadas por lanternas de fogo-fátuo presas em engrenagens de latão..."
        """, language="markdown")