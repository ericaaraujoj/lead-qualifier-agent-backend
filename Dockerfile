# 1. Imagem base do Python
FROM python:3.10-slim

# 2. Define o diretório de trabalho dentro do container
WORKDIR /code

# 3. Copia o arquivo de dependências
COPY requirements.txt .

# 4. Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copia todo o código do projeto para o container
COPY . .

# 6. Expõe a porta 8000 (que o FastAPI vai usar)
EXPOSE 8000

# 7. Comando padrão (será sobrescrito pelo docker-compose)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]