"""
Crie uma função que calcule a potência de um número.
A função deve aceitar dois argumentos, base e expoente.
Se o expoente não for fornecido ao chamar a função, ele deve ter o valor 2 como padrão.
"""

def potencia(base, expoente = 2):
    return base ** expoente

base_user = int(input('Digite o valor da base: '))
expoente_user = input('Digite o valor do expoente: ')

if expoente_user:
    print(f'O resultado é: {potencia(base_user, int(expoente_user))}')
else:
    print(f'O resultado é: {potencia(base_user)}')