# Dockerfile

# Imagem base Python
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia arquivo de dependências
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo o código da aplicação
COPY . .

# Comando para rodar a aplicação
CMD ["python","-u","app/src/main.py"]