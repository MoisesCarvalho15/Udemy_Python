"""
Crie um programa que peça o nome de uma cidade e verifique se
está presente na lista.
Se a cidade digitada não estiver, imprima: "Esta cidade não está na lista de cidades"
"""

cidades = ('São Paulo', 'Rio de Janeiro', 'Salvador')
cidade = input('Digite o nome da cidade: ')

if cidade in cidades:
    print('A cidade está presente na lista de cidades')
else:
    print('Esta cidade não está na lista de cidades')