""" Argumentos defaults
- Argumento que será default deverá ficar por último
- Caso contrário, irá dar erro no código
"""

def dados_pessoais(nome, sobrenome = 'Não informado'):
    print(f'Nome: {nome} \nSobrenome: {sobrenome}\n')

# Preenchendo todos os argumentos
dados_pessoais('Moisés', 'Carvalho')

# Não preenchendo o argumento sobrenome
dados_pessoais('Carlos')
