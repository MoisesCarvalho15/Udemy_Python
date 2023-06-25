# Criando listas a partir de inputs do usuário

frutas_usuario = input('Digite o nome das frutas separados por vírgula:\n')

# Criando uma lista separando os dados do input por vírgula e o espaço em branco
lista_frutas = frutas_usuario.split(', ')

print(lista_frutas)
