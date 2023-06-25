# Agregando duas listas com o Zip

produtos_estoque = ['Caneca', 'Copo', 'Jarra', 'Xícara']
quantidade_produtos = [2, 6, 7, 0]

agregando_listas = zip(produtos_estoque, quantidade_produtos)

# a função zip não retorna uma lista, retorna um objeto zip
print(agregando_listas)
# Imprimindo em formato de lista
print(list(agregando_listas))
