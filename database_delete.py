import mysql.connector
conexao = mysql.connector.connect(
    user= 'root',
    password='uniceub',
    host='127.0.0.1',
    database='db_empresa'
)

print('Conexão:',conexao)
cursor = conexao.cursor()
sql = '''
    select * from tb_funcionario 

'''
cursor.execute(sql)
registros = cursor.fetchall()     # Uma lista de tuplas, l_registros recebe os dados do select
print("Quantidade de registros na tabela:", cursor.rowcount)      #Quantidade de registros na tabela
print('- List of tuplas:')      #Solução 1, na horizontal
print(registros)
sql = '''
    delete from tb_funcionario where idt = 2


'''
cursor.execute(sql)
conexao.commit()
