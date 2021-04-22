import pandas as pd

def ObterColunas(df):
	"""
	Obtém as colunas do DataFrame passado como argumento.
	Return:
	- (list) colunas
	"""
    colunas = []

    for col in df.columns:
        colunas.append(col)
    
    return colunas

def ObterRegistros(df):
	"""
	Obtém a lista de valores do DataFrame.
	Return:
	- (list) registros
	"""
    registros = []

    for registro in df[:].values[:]:
        registros.append(tuple(registro))

    return registros

def GerarInsert(colunas, registros):
	"""
	Converte a lista de colunas e valores do DataFrame em
	uma string de código em SQL para INSERT.
	
	Return:
	- (str) inserts 
	"""
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
	"""
	Executa a conversão de um DataFrame para uma string com
	código SQL com INSERT.
	Return:
	- (str) insert
	"""
    colunas = ObterColunas(df)
    registros = ObterRegistros(df)
    insert = GerarInsert(colunas, registros)

    return insert

def GerarSql(df):
	"""
	Por que precisa dessa função?

	Return:
	- 
	"""
    # df = pd.read_csv('teste.csv', sep=';')
    sql = ConverterDados(df)

    return sql

if __name__ == '__main__':
    pass