import os
from dotenv import load_dotenv
import google.generativeai as genai
import streamlit as st
from google.generativeai.types import HarmCategory, HarmBlockThreshold



@st.cache_resource
def config_model():
    # api_key = st.secrets.get("GOOGLE_API_KEY")
    api_key = None
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            api_key = st.secrets["GOOGLE_API_KEY"]
    except (FileNotFoundError, KeyError, AttributeError):
        pass
    except Exception:
        pass
    
    if not api_key:
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        
    if not api_key:
        print("ERRO: API KEY não encontrada")
        return None
    
    try:
        genai.configure(api_key=api_key)
        generation_config = {
            'temperature' : 1,
            'top_p': .95,
            'top_k' : 64,
            'max_output_tokens': 2500,
            'candidate_count': 1,
            'response_mime_type': 'text/plain'
        }
        safety_setting = {
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_ONLY_HIGH,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_ONLY_HIGH,
        }
        
        model = genai.GenerativeModel(
            model_name='gemini-2.5-flash',
            generation_config=generation_config,
            safety_settings=safety_setting
        )
        return model
    except Exception as e:
        print(f"Erro interno na configuração: {e}")
        return None

    

def gerar_background_cidade(model, nome_cidade, sistema_rpg, localizacao_geral, vibe_principal, elemento_unico):

    prompt_final = f"""
    Você é um Mestre de Jogo (Dungeon Master) experiente e um escritor de fantasia criativo, agindo como um especialista no sistema de RPG **{sistema_rpg}**.

    Sua tarefa é criar uma descrição detalhada e inspiradora para uma cidade, baseada nas especificações do usuário. Organize a resposta usando os títulos abaixo. Ao criar os locais e ganchos de aventura, incorpore elementos, criaturas, facções e conceitos que são icônicos e mecanicamente relevantes para o sistema **{sistema_rpg}**.

    **Dados Fornecidos pelo Mestre:**
    - **Sistema de Referência:** {sistema_rpg}
    - **Localização no Mundo:** {localizacao_geral}
    - **Vibe Principal da Cidade:** {vibe_principal}
    - **Elemento Único e Intrigante:** {elemento_unico}

    ---

    ## Nome da Cidade: {nome_cidade}

    ### Descrição Geral
    (Parágrafo curto que captura a atmosfera da cidade, combinando a **vibe principal** de '{vibe_principal}' com a **localização** em '{localizacao_geral}'. Como ela se parece, cheira e soa?)

    ### Breve História e Lore
    (Um ou dois parágrafos sobre a origem da cidade. Um evento marcante, uma lenda local ou um segredo antigo que define sua identidade.)

    ### Governo e Poder
    (Quem manda na cidade? É um conselho de mercadores, um lorde tirano, uma guilda de magos, um líder religioso ou não há governo central? Se possível, conecte a uma facção conhecida em **{sistema_rpg}**.)

    ### Locais Notáveis (Descreva 3 a 5)
    (Crie locais interessantes. Se um local tiver um NPC importante, sugira sua classe ou conceito dentro de **{sistema_rpg}**.)
    1.  **[Nome do Local 1]:**
    2.  **[Nome do Local 2]:**
    3.  **[Nome do Local 3]:**

    ### Ganchos de Aventura (Crie 3)
    (Crie ideias de missões, problemas ou mistérios. Sugira quais testes de perícia de **{sistema_rpg}** poderiam ser úteis.)
    1.  **[Título do Gancho 1]:**
    2.  **[Título do Gancho 2]:**
    3.  **[Título do Gancho 3]:**
    """

    print("Gerando Legendas com IA ...")

    try:
        resposta = model.generate_content(prompt_final)
        return resposta.text
    except Exception as e:

        return f"Erro ao gerar conteúdo: {e}"
    
if __name__ == "__main__":
    modelo_gemini = config_model()
    if modelo_gemini:

        print("Por favor, forneça os detalhes para gerar suas cidades:\n")

        # Coletando informações do usuário
        nome_cidade = "Fortaleza do Sol Poente"
        sistema_rpg = "D&D 5e"
        localizacao_geral = "Numa costa de praias ensolaradas, onde um vasto sertão de cactos e areia encontra o mar azul-esverdeado"
        vibe_principal = "Porto comercial vibrante e caótico, cheio de jangadas mágicas e navios de reinos distantes"
        elemento_unico = "A cidade é famosa por suas 'Lágrimas de Iracema', cristais azuis encontrados na areia que podem armazenar pequenas magias. Isso gera uma disputa acirrada entre as guildas de mercadores e os nativos Tupi, que consideram os cristais sagrados."

        # Chamando a função para gerar as legendas
        legendas_geradas = gerar_background_cidade(
            model=modelo_gemini,
            nome_cidade=nome_cidade,
            localizacao_geral = localizacao_geral,
            sistema_rpg=sistema_rpg,
            vibe_principal=vibe_principal,
            elemento_unico=elemento_unico
        )

        # Exibindo o resultado final
        print("\n---O PERGAMINHO DA CIDADE ESTÁ PRONTO! ---")
        print(legendas_geradas)
