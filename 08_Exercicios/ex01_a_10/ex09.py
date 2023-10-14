"""
Crie um programa que remova a frutas "manga" e o último item.
Utilize a lista com os itens modificados no exercício anterior.
Imprima a lista original e a modificada.
"""

frutas = ['Maçã', 'Morango', 'Manga', 'Uva', 'Abacaxi']

print(frutas)

# Removendo itens da lista
frutas.remove("Manga")
del frutas[-1]

print(frutas)