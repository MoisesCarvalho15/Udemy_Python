"""
Crie um programa que verifique os números de uma lista se são par ou ímpar.
A lista deverá ser de 1 a 10.
Itere sobre a lista e para cada número, imprima:
O número "x" é PAR! ou O número "x" é ímpar
"""

numeros = list(range(1, 11))

for numero in numeros:
    if numero % 2 == 0:
        print(f'O número {numero} é par!')
    else:
        print(f'O número {numero} é ímpar!')
