import mysql.connector
conexao = mysql.connector.connect(
    user= 'root',
    password='uniceub',
    host='127.0.0.1',
    database='db_empresa'
)

print('Conexão:',conexao)
cursor = conexao.cursor()
sql = """
    insert into tb_funcionario
    (idt, nome, salario)
    values 
    (1, 'João', 2500.00),
    (2, 'Matheus', 4000.00)
"""
cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()
