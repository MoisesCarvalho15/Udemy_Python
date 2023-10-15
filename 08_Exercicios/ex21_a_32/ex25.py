"""
Crie uma função que aceite dois números como entrada e retorne a soma desses números.
"""

def soma(n1,n2):
    return n1 + n2

num1 = float(input('Digite um número: '))
num2 = float(input('Digite outro número: '))

print(f'{num1} + {num2} = {soma(num1, num2)}')