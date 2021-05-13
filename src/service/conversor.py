import pandas as pd
import codecs
import os

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

def GerarInsert(colunas, nomeTabela, registros):
	"""
	Converte a lista de colunas e valores do DataFrame em
	uma string de código em SQL para INSERT.

	Return:
	- (str) inserts 
	"""
	header = f'insert into {nomeTabela} ({", ".join(colunas)}) values' 
	body = ' '

	for reg in registros:
		if reg != registros[-1]:
			body += f'{reg},\n'
		else:
			body += f'{reg};\n'

	insert = header + body
	return insert

def GerarSql(df, nomeTabela):
	"""
	Executa a conversão de um DataFrame para uma string com
	código SQL com INSERT.
	Return:
	- (str) insert
	"""
	#verificar se não existe algum .sql salvo. Caso exista, exlcuir
	
	colunas = ObterColunas(df)
	registros = ObterRegistros(df)
	insert = GerarInsert(colunas, nomeTabela, registros)

	diretorio = os.listdir('service/sql')
	if len(diretorio) > 0:
		for arquivo in diretorio:
			os.remove(f'service/sql/{arquivo}')

	file = codecs.open(f'service/sql/insert_{nomeTabela}.sql', 'w', 'utf-8')
	sql = insert.replace(', \'', ', \"').replace('\',', '\",').replace('\'),', '\"),').replace('\');', '\");')
	file.write(sql)
	file.close()

	return sql

if __name__ == '__main__':
	pass