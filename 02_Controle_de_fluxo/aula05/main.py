# For loop - Utilizando números
# OBS: A contagem vem do index. Considerar um número a mais do desejado

print('Primeiro exemplo:')
# Imprimindo de 0 até o número 4
for numero in range(5):
    print(numero)

print('Segundo exemplo:')
# Escolhendo o ponto de início do loop
for numero in range(3, 6): # vai do 3 até o 5
    print(numero)

print('Terceiro Exemplo:')
# "Pulando" casas do index até o número desejado
for numero in range(0, 11, 2): # Parâmetros são: Início, fim -1, passos.
    print(numero)
