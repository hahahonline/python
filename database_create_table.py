
import mysql.connector
conexao = mysql.connector.connect(
    user='root',            #user do servidor
    password='uniceub',      #passwd do seu servidor local
    host='127.0.0.1',       #host = 'localhost'
    database='db_empresa'
)

print('Conexao:', conexao)          #Testando
cursor = conexao.cursor()           #Cria o cursor para executar comandos SQL

# sql = 'CREATE DATABASE if not exists db_empresa'  #o database já foi criado, logo não precisa dessa linha
# cursor.connect(sql)

sql = '''
    CREATE TABLE IF NOT EXISTS tb_funcionario(
    idt INT,
    nome VARCHAR(45) NOT NULL,
    salario DECIMAL(9,2) NULL,      #O Null é opcional
    PRIMARY KEY(idt)
    )
'''

cursor.execute(sql)
cursor.close()
cursor.close()
print('\nConexão fechada.')
