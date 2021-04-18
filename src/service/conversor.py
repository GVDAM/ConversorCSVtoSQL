import pandas as pd
import os

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

def GerarInsert(colunas, registros, nomeTabela):
    header = f'insert into {nomeTabela}\n({", ".join(colunas)})\nvalues\n'
    body = ''

    for reg in registros:
        if reg != registros[-1]:
            body += f'{reg},\n'
        else:
            body += f'{reg};\n'

    insert = header + body
    return insert

def ConverterDados(df, nomeTabela):
    colunas = ObterColunas(df)
    registros = ObterRegistros(df)
    insert = GerarInsert(colunas, registros, nomeTabela)
    print('ConverterDados: ' + insert)

    return insert

def GerarSql(df, nomeTabela):
    # df = pd.read_csv('teste.csv', sep=';')
    sql = ConverterDados(df, nomeTabela)
    print('GerarSql: ' + sql)
    #verificar se não existe algum .sql salvo. Caso exista, exlcuir
    file = open(f'insert_{nomeTabela}.sql', 'w')
    file.write(sql.replace(' \'', ' \"').replace('\',', '\",').replace('\')', '\")'))
    file.close()
    return sql

if __name__ == '__main__':
    GerarSql()