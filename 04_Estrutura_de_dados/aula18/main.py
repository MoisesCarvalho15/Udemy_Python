# Generator Expression
    # Forma mais rápida para Listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes
    
from sys import getsizeof

# Lista
numeros = [numero * 10 for numero in range(20)]
print(f'Tipo do dado: {type(numeros)}')
print(f'Quantidade de memória utilizada: {getsizeof(numeros)} bytes \n')

# Generator Expression
numeros2 = (numero * 10 for numero in range(20))
print(f'Tipo do dado: {type(numeros2)}')
print(f'Quantidade de memória utilizada: {getsizeof(numeros2)} bytes')
