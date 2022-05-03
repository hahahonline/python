import sqlite3 #Importa biblioteca
database = 'livraria.db' #
conexao = sqlite3.connect(database) #Conexão do programa com banco de dados
cur = conexao.cursor() #Criação de um cursor para executar comandos sql



sql = ''' CREATE table if not exists tb_cliente(
 cpf text primary key, nome text not null,
 idade integer)'''


cur.execute(sql)






cur.close()
conexao.close()
