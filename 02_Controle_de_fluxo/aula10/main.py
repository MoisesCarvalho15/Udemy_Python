# For loop - Criando um tabuleiro

# Criando um tabuleiro 6x6
linhas = 3
colunas = 6
simbolo = '*'


for linha in range(linhas):
    for coluna in range(colunas):
        print(simbolo, end='')
    print()
