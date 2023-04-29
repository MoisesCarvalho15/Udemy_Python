# Métodos para Strings

mensagem = 'eu estou aprendendo Python!'

# tudo em letras minúsculas
print(mensagem.lower())

# tudo em letras maiúsculas
print(mensagem.upper())

# a primeira letra do texto em maiúscula
print(mensagem.capitalize())

# procurando por letra ou palavra. O retorno será o index
print(mensagem.find('y'))
print(mensagem.find('Python'))

# trocando letra ou palavra
print(mensagem.replace('p', 'P'))
print(mensagem.replace('estou', 'estava'))

# removendo o espaço ante da primeira letra
mensagem2 = f'           {mensagem}' # adicionei os espaços para o exemplo
print(mensagem2)
print(mensagem2.strip())