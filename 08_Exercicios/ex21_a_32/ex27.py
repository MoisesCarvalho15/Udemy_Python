"""
Crie uma função que faça o fatorial de um número.
"""

def fatorial(n):
    if n == 0 or n == 1:
        return 1    
    else:
        return n * fatorial(n -1)

num = int(input("Digite um número: "))

print(f"O fatorial do número {num} é = {fatorial(num)}")
