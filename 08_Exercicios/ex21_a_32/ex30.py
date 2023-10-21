"""
Crie uma função lambda que aceite dois números e retorne a multiplicação desses números.
"""

mult = lambda n1, n2: n1 * n2

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

print(f"{num1} x {num2} = {mult(num1, num2)}")
