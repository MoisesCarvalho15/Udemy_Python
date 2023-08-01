# List comprehension com números
# fazer uma lista que cresça com os valores de 10 em 10 começando do 0. Fazendo isso 6 vezes

valores = []

for valor in range(6):
    valores.append(valor * 10)
    
print(valores)

# Resolvendo utilizando list comprehension
valores2 = [valor * 10 for valor in range(6)]
print(valores2)