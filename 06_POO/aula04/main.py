# Adicionando mais funções na classe
# Importando módulo
from datetime import datetime

class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento
    
    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    def idade_funcionario(self):
        ano_atual = datetime.now().year
        idade = ano_atual - self.ano_nascimento
        return idade

# Criando objetos
user1 = Funcionarios('Elena', 'Cabral', 2009)
user2 = Funcionarios('Carol', 'Silva', 1999)

# Imprimindo dados
print(Funcionarios.nome_completo(user1))
print(Funcionarios.idade_funcionario(user1))

print(Funcionarios.nome_completo(user2))
print(Funcionarios.idade_funcionario(user2))