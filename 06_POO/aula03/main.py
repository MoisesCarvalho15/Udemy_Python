# Criando construtores

class Funcionarios:
    def __init__(self, nome, sobrenome, data_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.data_nascimento = data_nascimento

# Criando objetos
user1 = Funcionarios('Elena', 'Cabral', '12/02/2009')
user2 = Funcionarios('Carol', 'Silva', '15/10/1999')

# Imprimindo dados
print(user1.nome)
print(user2.nome)