# Função Map com lambda

numeros = [1, 2, 3, 4, 5]

def multiplica_Numeros_listas(numero):
    return numero * 2
    
resultado = map(multiplica_Numeros_listas, numeros)
resultado2 = map(lambda x: x * 2, numeros)

print(f'Função map: {list(resultado)}')
print(f'Lambda com o map: {list(resultado2)}')
