# List Comprehension com letras
# Usado quando precisamos criar uma nova lista a partir de uma existente.

nomes = ['Moisés', 'Henrique', 'Elisabeth', 'Anna', 'Carlos']
nomes2 = []

# selecionando nomes que contém uma letra específica
for nome in nomes:
    if 'a' in nome:
        nomes2.append(nome)

print(nomes2)

# Outra maneira de resolver
nomes3 = [nome for nome in nomes if 'e' in nome]

print(nomes3)