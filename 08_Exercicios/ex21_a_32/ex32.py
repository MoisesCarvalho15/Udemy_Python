"""
Crie uma função lambda que eleve um número ao quadrado.
Em seguida, use essa função para calcular o quadrado de todos os números de uma lista.
"""

numeros = [1, 2, 3, 4, 5, 6]

quadrado = lambda n: n ** 2
quadrado_numeros = list(map(quadrado, numeros))

print(quadrado_numeros)
