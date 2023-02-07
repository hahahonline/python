class Aluno:    #Declaração da classe Aluno
    def __init__(self, aluno, nota): #Método construtor da classe, que será chamado automaticamente quando uma nova instância for criada.
        # Ele tem dois parâmetros, aluno e nota, que serão usados para inicializar os atributos da instância.

        self.aluno = aluno #Atribuição do valor do parâmetro aluno ao atributo aluno da instância.
        self.nota = nota #Atribuição do valor do parâmetro nota ao atributo nota da instância.
    def __str__(self):
        return f'Nome: {self.aluno} \n Nota: {self.nota}'


alunos = [ #Criação de uma lista chamada alunos
    Aluno("João", 8), #Adição de uma instância da classe Aluno na lista alunos, com o nome "João" e nota 9.
    Aluno("Maria", 7.5),#idem
    Aluno("Carlos", 3.5),#idem
    Aluno("Daniel", 4.5),#idem
    Aluno("Bia", 6.5)#idem
] #Fim da lista alunos

soma_notas = 0  #Inicialização de uma variável

for aluno in alunos:  #Início de um laço for, que percorre a lista alunos
    soma_notas += aluno.nota #Adição do valor da nota do aluno corrente (aluno.nota) à variável soma_notas.

media = soma_notas / len(alunos) #Cálculo da média das notas, dividindo a soma de todas as notas (soma_notas) pelo número de alunos (len(alunos)).

for aluno in alunos:
    print("Aluno:", aluno.aluno, "| Nota:", aluno.nota)
print("\nA média das notas é: {}".format(media)) #Impressão da média das notas.
