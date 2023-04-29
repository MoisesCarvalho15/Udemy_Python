'''
- Praticando com Strings e Integers

1. Na frase: "O André tem 32 anos de idade e mora na cidade de São Paulo.". 
    1.1. Crie variáveis que possam ser alteradas, como: Nome, Idade e Cidade.
    1.2. Crie interações com o usuário e faça com que os dados inseridos modifique as variáveis da frase.
'''

nome = input('Qual é o seu nome:    ')
idade = input('Qual é a sua idade: ')
cidade = input('Qual a sua cidade: ')

print('O ' + nome + ' tem ' + str(idade) + ' anos de idade e mora na cidade de ' + cidade + '.')
