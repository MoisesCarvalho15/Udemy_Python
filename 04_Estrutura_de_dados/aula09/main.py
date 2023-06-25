# Utilizando set

lista1 = [10, 20, 30, 40]
lista2 = [10, 20, 50, 60]

# Set - O index da lista passada não será o mesmo
set_lista1 = set(lista1) 
set_lista2 = set(lista2)

# Union - Retorna os valores sem ter os duplicados
union = set_lista1 | set_lista2
# Difference - Retorna os valores que não são duplicados
difference = set_lista1 - set_lista2
# Symmetric Difference - Retorna a lista removendo os valores duplicados
symmetric_difference = set_lista1 ^ set_lista2
# And - Retorna os valores duplicados
and_list = set_lista1 & set_lista2

print(union)
print(difference)
print(symmetric_difference)
print(and_list)