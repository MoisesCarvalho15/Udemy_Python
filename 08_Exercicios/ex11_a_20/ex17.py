"""
Crie um programa que verifique a idade do usuário.
Para cada condição, deverá ser imprimida uma mensagem na tela.
Menor que 13: "Você é uma criança"
Entre 13 e 19: "Você é um adolescente"
Maior que 20: "Você é um adulto"
"""

idade = int(input('Digite sua idade: '))

if idade < 13:
    print("Você é uma criança!")
elif idade in range(13, 20):
    print('Você é um adolescente!')
else:
    print('Você é um adulto!')