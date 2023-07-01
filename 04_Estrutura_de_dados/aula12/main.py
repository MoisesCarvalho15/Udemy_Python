# Atualizando dados de um dicionário

aluno = {'nome': 'Moisés', 'idade': 22}

# Primeira forma para mudar o valor de uma key
aluno['nome'] = 'Carlos'
print(aluno)

# Segunda forma para mudar o valor da key
# Podemos mudar mais de um valor do dicionário
aluno.update({'nome': 'Anna', 'idade': 20})
print(aluno)

# Adicionando uma nova key e um novo value
aluno.update({'Altura': 1.65})
print(aluno)

# Buscando um valor sem gerar erro no programa
# Podemos adicionar uma mensagem de retorno caso a key não for encontrada
endereco = aluno.get('Endereço', 'Valor de Chave não encontrada.')
print(endereco)

# Removendo chave e valor
del aluno['idade']
print(aluno)
