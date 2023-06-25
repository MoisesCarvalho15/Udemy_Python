# Verificando itens em uma lista

cores = ['Amarelo', 'Azul', 'Preto', 'Branco']

cor = input('Digite uma cor: ').capitalize()

if cor in cores:
    print(f'A cor "{cor}" está presente na lista de cores.')
else:
    print(f'A cor "{cor}" NÃO está na lista de cores.')
