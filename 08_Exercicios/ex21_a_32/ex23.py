"""
Crie um programa que identifique quais estão presentes em dois conjuntos separados.
Crie dois conjuntos, cada um contento 5 nomes.
Alguns nomes devem estar presente em ambos os conjuntos. Imprima esses nomes.
"""

nomes1 = {'Carlos', 'João', 'Maria', 'Lucia', 'Joaquim'}
nomes2 = {'Moisés', 'Amanda', 'João', 'Carlos', 'Sabrina'}

nomes_repetidos =  list(nomes1.intersection(nomes2))

print(nomes_repetidos)