# Try, Except, Else e Finally com o input do usuário

try:
    # Transformando o input em um valor float
    valor_produto = float(input('Digite o valor do produto: '))
except ValueError:
    print('Por favor, verifique o valor digitado.')
else:
    # Este bloco de código será executado apenas se a condição
    # do try ser verdadeira.
    print(f'Total: R${valor_produto}')


# Utilizando o finally
try:
    numero = int(input('\nDigite um número: '))
except ValueError:
    print('Verifique o valor digitado.')
finally:
    print(f'Número digitado: {numero}')
    print('Independente do resultado, este bloco de código será executado.')