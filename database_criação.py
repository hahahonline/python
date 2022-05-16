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
l_registros = cursor.fetchall()     # Uma lista de tuplas, l_registros recebe os dados do select
print("Registros na tabela:", cursor.rowcount)      #Quantidade de registros na tabela
print('- List of tuplas:')      #Solução 1, na horizontal
# for row in l_registros:         #Mostra os valores na vertical, pq ele percorre valor por valor no for
#     print("\nIdt:" ,row[0])
#     print("Nome:" ,row[1])
#     print("Salário:" ,row[2])
# print(l_registros)            #Mostra os valores na horizontal
for idt, nome, grana in l_registros:         #Mostra os valores na vertical, através das variaveis que são identificadas pela ordem que foram feitas
    print("\nIdt:" ,idt)
    print("Nome:" ,nome)
    print("Salário:" , grana)
cursor.close()
conexao.close()
print('\nConexão fechada.')
