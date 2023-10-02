"""Filtrando funcionários com 'Sets'
Criar um programa que gere 3 listas de acordo com a necessidade abaixo:

Lista 1 = Funcionários que tem carro e trabalham a noite
Lista 2 = Funcionários que tem carro e trabalham durante o dia
Lista 3 = Funcionários que não tem carro
"""

# Dados dos funcionários
funcionarios = ['Ana', 'Marcos', 'Alice', 'Pedro', 'Sophia', 'Bruno', 'Melissa']
turno_dia = ['Ana', 'Marcos', 'Alice', 'Melissa']
turno_noite = ['Pedro', 'Sophia', 'Bruno']
tem_caro = ['Marcos', 'Alice', 'Bruno', 'Melissa']

# Tem carro e trabalham a noite
lista1 = list(set(turno_noite) & set(tem_caro))
print(f'Funcionários que trabalham a noite e tem carro: {lista1}\n')

# Tem carro e trabalham de dia
lista2 = list(set(turno_dia) & set(tem_caro))
print(f'Funcionários que trabalham de dia e tem carro: {lista2}\n')

# Não tem carro
lista3 = list(set(funcionarios) - set(tem_caro))
print(f'Funcionários que não tem carro: {lista3}\n')
