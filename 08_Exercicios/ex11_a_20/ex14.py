"""
Crie um programa que tenha dois loops que imprima os números de 1 a 10.
O primeiro loop deve parar de imprimir assim que chegar no número 5.
O segundo, deverá pular a impressão do número 5.
"""

print('Loop com Break')
for numero in range(1, 11):
    if numero > 5:
        break
    print(numero)

print('\nLoop com Continue')
for num in range(1, 11):
    if num == 5:
        print('Pulou')
        continue
    print(num)