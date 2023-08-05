# Try e Except com uma lista

letras = ['A', 'B', 'C']

try:
    # Pegando um index que não existe
    print(letras[3])
except IndexError:
    print('Index não existe')