"""
Crie um programa que verifica se tem um determinado carro no estoque.
Peça ao usuário digitar o carro desejado.
Utilize os seguintes carros na lista: BMW X6, BMW i5, BMW i8.
Se estiver em estoque, imprima: "Este carro está disponível!"
Se não estiver em estoque, imprima: "Este carro não está disponível!"
"""

carros = ['BMW X6', 'BMW i5', 'BMW i8']

carro = input('Digite o nome carro desejado: ')

if carro in carros:
    print('Este carro está disponível!')
else:
    print('Desculpe, este carro não está disponível!')
    