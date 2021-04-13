from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import BytesIO

# Instancia um objeto para iniciar a aplicação
app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    """
	Função assíncrona que recebe um arquivo.
    """
    # O arquivo uploaded é lido como um 
    contents = await file.read()
    # O conteúdo do arquivo é convertido em Bytes
    arquivo = BytesIO(contents)
    # O arquivo convertido é transformado em DataFrame
    df = pd.read_csv(arquivo)
    print(type(contents))
    print(type(arquivo))
    print(df)

    return { 'file.name': file.filename, 
             'dataFrame': df[:1].values[0][0][0] }