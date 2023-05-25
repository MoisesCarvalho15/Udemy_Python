# Funções dentro de listas

numeros = [1, 2, 3]
print(f'\nPrimeira versão da lista: {numeros}')

# Adicionando um item no final da lista
numeros.append(4)
print(f'\nSegunda versão da lista: {numeros}')

# Removendo um item da lista através do valor contido na lista
numeros.remove(1)
print(f'\nTerceira versão da lista: {numeros}')

# Adicionando um item no local exato da lista
numeros.insert(2, 55) # index 2 valor 55
print(f'\nQuarta versão da lista: {numeros}')

# Retirando um item da lista através do index
numeros.pop(0)
print(f'\nQuinta versão da lista: {numeros}')

# Organizando em ordem
numeros.sort()
print(f'\nSexta versão da lista: {numeros}')
