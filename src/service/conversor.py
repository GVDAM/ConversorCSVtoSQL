import pandas as pd

def ObterColunas(df):
    colunas = []

    for col in df.columns:
        colunas.append(col)
    
    return colunas

def ObterRegistros(df):
    registros = []

    for registro in df[:].values[:]:
        registros.append(tuple(registro))

    return registros

def GerarInsert(colunas, registros):
    header = f'insert into table ({", ".join(colunas)}) values'
    body = ' '

    for reg in registros:
        if reg != registros[-1]:
            body += f'{reg},'
        else:
            body += f'{reg};'

    inserts = header + body
    return inserts

def ConverterDados(df):
    colunas = ObterColunas(df)
    registros = ObterRegistros(df)
    insert = GerarInsert(colunas, registros)

    return insert

def GerarSql(df):
    # df = pd.read_csv('teste.csv', sep=';')
    sql = ConverterDados(df)

    return sql

if __name__ == '__main__':
    pass