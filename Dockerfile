# Dockerfile

# 1. Imagem Base: Começamos com uma imagem oficial e leve do Python.
FROM python:3.10-slim

# 2. Diretório de Trabalho: Define o diretório padrão dentro do contêiner.
WORKDIR /app

# 3. Copiar e Instalar Dependências:
# Copiamos APENAS o requirements.txt primeiro. O Docker é inteligente e só
# vai re-executar este passo se este arquivo mudar, acelerando builds futuros.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copiar o Resto do Código: Agora copiamos todos os outros arquivos do projeto.
COPY . .

# 5. Expor a Porta: Informa ao Docker que a aplicação dentro do contêiner
# vai rodar na porta 8501 (porta padrão do Streamlit).
EXPOSE 8501

# 6. Comando de Execução: Este é o comando que será executado quando
# o contêiner iniciar.
CMD ["streamlit", "run", "app.py"]