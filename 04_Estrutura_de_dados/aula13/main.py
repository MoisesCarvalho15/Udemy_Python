# Loops dentro do dicionário

dicionario = {'Chave1': 'Valor 1', 'Chave2': 'Valor 2', 'Chave3': 'Valor 3'}

# Primeira maneira de imprimir somente as chaves do dicionário
print('Imprimindo as chaves do dicionário:')
for i in dicionario:
    print(i)

# Segunda maneira de imprimir somente as chaves
print('\nImprimindo outra vez as chaves do dicionário:')
for i in dicionario.keys():
    print(i)

# Imprimindo somente os valores
print('\nImprimindo os valores:')
for i in dicionario.values():
    print(i)

# Imprimindo as chaves e os valores
print('\nImprimindo as chaves e valores:')
for chaves, valores in dicionario.items():
    print(chaves, valores)