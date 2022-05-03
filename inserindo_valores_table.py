import sqlite3
conexao = sqlite3.connect('livraria.db')
cur = conexao.cursor()

#MANEIRA 1 DE INCLUIR VALOR
# sql = """insert into tb_cliente(cpf,nome,idade)
# values('162','Paulo',31)"""
#
# cur.execute(sql)
# conexao.commit()
#
#MANEIRA 2 DE INCLUIR VALOR
# sql = "insert into tb_cliente(cpf, nome, idade) values('161','João','21')"
# cur.execute(sql)
# conexao.commit()

#MANEIRA 3 DE INCLUIR VALOR
# sql = "insert into tb_cliente(cpf, nome) values('163','Maria')"
# cur.execute(sql)
# conexao.commit()

#MANEIRA 4 DE INCLUIR VALOR (nesse caso, damos a opção ao usuário para passar os valores)
# sql1 = "insert into tb_cliente(cpf, nome, idade) values (?,?,?)"
# v_cpf = input("CPF: ")
# v_nome = input("Nome: ")
# v_idade = input("Idade: ")
# cur.execute(sql1, (v_cpf, v_nome, v_idade)) #os parenteses sao obrigatorios


sql = "insert into tb_cliente values ('202', 'Ezequiel', '30')"
cur.execute(sql)
conexao.commit()

print("Qtd. registros inseridos-rowcount:", cur.rowcount) #Qtd de registros inseridos (1)
print("Qtd. registros na base-lastrowid", cur.lastrowid) #Qtd de registros na base (n)



conexao.commit()

conexao.close()
