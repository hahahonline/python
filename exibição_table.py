"""

Sintaxe:

sql = "select (* | nome_coluna1, nome_coluna1, ...) from nome_tabela"
"""

import sqlite3

conexao = sqlite3.connect('livraria.db')  # Como esse database já existe, ele só vai se conectar nele
cur = conexao.cursor() #  Cria um cursor para executar os comandos sql

sql = 'select * from tb_cliente' # Consulto a tabela tb_cliente
cur.execute(sql) # Vai executar o sql
registros = cur.fetchall() # Pega o resultado do select e coloca na lista registros (registros é o nome da variavel que criei, ela vai ser criada como lista)
print(registros)


cur.close() # Vai encerrar o executador de comandos sql
conexao.close() # Vai encerrar a conexão
