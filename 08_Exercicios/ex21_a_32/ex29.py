"""
Crie uma função Lambda que aceite um número e retorne o cubo desse número.
"""

numero = int(input("Digite um número: "))

cubo = lambda x: x ** 3

print(f"O cubo do número {numero} é = {cubo(numero)}")
