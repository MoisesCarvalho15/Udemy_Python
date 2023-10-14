"""
Crie um programa que peça ao usuário um número.
Imprima na tela uma mensagem dizendo se esse número é:
menor ou igual a 10. Ou se esse número é maior que 10
"""

num = float(input('Digite um número: '))

if num <=10:
    print(f'O número {num} é MENOR ou IGUAL a 10!')
else:
    print(f'O número {num} é MAIOR que 10!')
