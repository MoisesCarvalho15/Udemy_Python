"""
Crie uma função que aceite um número como entrada e retorne o quadrado desse número.
"""

def num_quadrado(numero):
    return numero ** 2

num1 = float(input('Digite um número: '))

print(f'O quadrado de {num1} = {num_quadrado(num1)}')
