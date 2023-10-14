"""
Crie um programa que solicite ao usuário dois números.
O programa deverá imprimir: soma, subtração, multiplicação,
divisão e exponenciação desses números.
A exponenciação deverá ser o primeiro número elevado ao segundo
digitado pelo usuário.
"""

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
expo = num1 ** num2

print(f'{num1} + {num2} = {soma}')
print(f'{num1} - {num2} = {sub}')
print(f'{num1} * {num2} = {mult}')
print(f'{num1} / {num2} = {div}')
print(f'{num1} ** {num2} = {expo}')