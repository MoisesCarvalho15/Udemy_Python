"""
Crie um programa e inclua um item três vezes dentro da lista.
Utilize um loop para contar quantas vezes esse item aparece na lista.
Imprima o resultado.
"""

lista = ['Viagem', 'Casa', 'Viagem', 'Viagem', 'Carro', 'Moto']
contador = 0

for item in lista:
    if item == 'Viagem':
        contador += 1

print(f'O palavra "Viagem" apareceu {contador} vezes na lista!')
