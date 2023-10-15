"""
Crie um programa que através do país digitado pelo usuário, retorne a sua capital.
Crie um lista com 5 nomes de países e suas capitais.
Se o país digitado estiver na lista, imprima: "[país] tem como capital [capital]."
Se não tiver na lista, imprima: "Desculpe, não temos informações sobre a capital desse país."
"""

paises_capitais = {
    'Alemanha': 'Berlim', 
    'Portugal': 'Lisboa', 
    'Brasil': 'Brasília', 
    'USA': 'Washington, D.C', 
    'Egito': 'Cairo'
}

pais = input('Digite o nome de um país: ')

if pais in paises_capitais:
    print(f'{pais} tem como capital {paises_capitais[pais]}.')
else:
    print('Desculpe, não temos informações sobre a capital desse país.')