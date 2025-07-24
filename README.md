# Forja de Mundos - Gerador de Cenários de RPG

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.36-red?style=for-the-badge&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-20.10+-blue?style=for-the-badge&logo=docker)
![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=for-the-badge)

Uma aplicação web construída com Python, Streamlit e a API do Google Gemini para gerar cenários de cidades detalhadas para diversas campanhas de RPG, ajudando Mestres de Jogo a superar o bloqueio criativo.

---

### Demonstração Rápida

*(DICA: Grave um GIF de 15-20 segundos mostrando você preenchendo os campos e o resultado aparecendo na tela. Depois, adicione o GIF a esta pasta e troque o link abaixo)*

![Demonstração da Aplicação](caminho/para/seu/demo.gif)

---

### Sobre o Projeto

Como Mestre de RPG, sei que uma das tarefas mais demoradas e desafiadoras é a criação de cenários vibrantes e cheios de vida. A "Forja de Mundos" nasceu para resolver esse problema. Esta ferramenta utiliza o poder da Inteligência Artificial Generativa (através da API Gemini do Google) para construir a fundação de uma cidade em segundos.

Basta fornecer alguns parâmetros criativos, e a IA irá gerar uma descrição completa, incluindo história, locais notáveis e ganchos de aventura, tudo formatado e pronto para ser usado na sua próxima sessão de jogo.

---

### Features

* **Geração de Cidades Detalhadas:** Cria descrições, história, governo, locais notáveis e ganchos de aventura.
* **Adaptação a Sistemas:** O conteúdo gerado se adapta a diferentes sistemas de RPG (D&D 5e, Tormenta20, etc.), usando conceitos e termos relevantes.
* **Interface Web Interativa:** Construído com Streamlit para uma experiência de usuário amigável e intuitiva.
* **Cache Inteligente:** Utiliza o cache do Streamlit (`@st.cache_resource` e `@st.cache_data`) para otimizar a velocidade e reduzir custos de API em requisições repetidas.
* **Exportação de Cenários:** Permite baixar o background da cidade gerada em formato Markdown (`.md`) com um único clique.
* **Conteinerizado com Docker:** O projeto é totalmente conteinerizado, garantindo um setup e execução consistentes em qualquer máquina com o Docker instalado.
* **Orquestração Simplificada:** Utiliza `docker-compose` para que a aplicação possa ser iniciada com um único comando (`docker-compose up`).

---

### Tecnologias Utilizadas

* **Backend:** Python
* **Interface Web:** Streamlit
* **Inteligência Artificial:** Google Gemini API
* **Conteinerização:** Docker & Docker Compose
* **Gerenciamento de Segredos:** python-dotenv

---

### Como Executar o Projeto

Para rodar este projeto localmente, você precisará ter o **Git** e o **Docker Desktop** instalados.

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/CarlosFranchN/Forja-de-Cidades-RPG.git
    cd https://github.com/CarlosFranchN/Forja-de-Cidades-RPG.git
    ```

2.  **Configure suas credenciais:**
    Crie uma cópia do arquivo `.env.example` (ou crie um novo arquivo) e renomeie para `.env`. Em seguida, adicione sua chave da API do Google.
    ```
    # .env
    GOOGLE_API_KEY="SUA_CHAVE_SUPER_SECRETA_AQUI"
    ```

3.  **Inicie a aplicação com Docker Compose:**
    Este comando irá construir a imagem Docker (na primeira vez) e iniciar o contêiner da aplicação.
    ```bash
    docker-compose up
    ```

4.  **Acesse a aplicação:**
    Abra seu navegador e acesse `http://localhost:8501`.

---

### Estrutura do Projeto

```
.
├── .env                  # Arquivo de variáveis de ambiente (local, ignorado pelo Git)
├── .gitignore            # Arquivos e pastas a serem ignorados pelo Git
├── Dockerfile            # Receita para construir a imagem Docker da aplicação
├── README.md             # Este arquivo
├── main.py                # Código da interface Streamlit
├── assistente_mestre.py    # Módulo com a lógica de IA e configuração do modelo
├── docker-compose.yml    # Arquivo de orquestração dos contêineres
└── requirements.txt      # Lista de dependências Python
```

---

### Próximos Passos e Melhorias

* [ ] Gerador de NPCs (Personagens Não-Jogáveis) para as cidades criadas.
* [ ] Gerador de Itens Mágicos ou Tavernas.
* [ ] Integração com uma API de geração de imagens para criar um "retrato" da cidade.
* [ ] Deploy da aplicação na nuvem (ex: Google Cloud Run, Streamlit Community Cloud).

---
