"""
Crie um função lambda que aceite um número e retorne "Par" or "Ímpar"
"""

par_ou_impar = lambda n: "Par" if(n % 2 == 0) else "Ímpar"

num = int(input("Digite um número: "))

print(f"O número {num} é {par_ou_impar(num)}")
