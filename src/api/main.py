from fastapi import FastAPI
from fastapi import FastAPI, File, UploadFile
import pandas as pd
from io import BytesIO

app = FastAPI()

@app.post("/files/")
async def create_file(file: UploadFile = File(...)):
    contents = await file.read()
    arquivo = BytesIO(contents)
    df = pd.read_csv(arquivo)

    sql = GerarSql(df)

    return { 'file.name': file.filename, 
             'dataFrame': df[:] ,
             'SQL': sql}