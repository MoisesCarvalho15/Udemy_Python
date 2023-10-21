"""
Crie um programa que contenha duas funções.
A primeira função deverá receber um número e retornar o dobro dele.
A segunda função deverá receber um número e retornar o quadrado dele.
Em seguida, chame a primeira função dentro da segunda para retornar o quadrado do dobro de um número.
"""

def dobro(n):
    return n * 2

def quadrado(n):
    return n ** 2

numero = int(input("Digite um número: "))

print(f"O dobro de {numero} é = {dobro(numero)}")
print(f"O quadrado de {numero} é = {quadrado(numero)}")
print(f"O quadrado do dobro de {numero} é = {quadrado(dobro(numero))}")