# Funções dentro de set

lista = set([1, 2, 3, 4, 5])

# Adicionando valores a list
lista.add(6)

# Mesmo se já conter o valor dentro da lista, o valor não será duplicado
lista.add(2)
print(lista)

# Adicionando mais de um valor
lista.update([7, 8, 9, 10])
print(lista)

# Removendo um valor
lista.remove(10)
print(lista)

# Tentando remover um valor não existente
lista.discard(100) # Essa função NÃO retorna um erro
print(lista)