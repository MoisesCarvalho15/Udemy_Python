# Entendendo o Slice

# index  01234567....
fruta = 'Melancia'
numero = 22.68

# pegando somente uma letra da palavra
print(fruta[1])
# pegando um conjunto de letras
print(fruta[0:5])
# pegando letras com número negativo
print(fruta[0:-3])

# No código abaixo tem um erro
# print(numero[3])
numero = str(numero)
print(numero[3])
