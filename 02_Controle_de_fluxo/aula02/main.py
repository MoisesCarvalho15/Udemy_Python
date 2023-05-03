# Operadores Lógicos
# and -> só retorna TRUE se ambas as condições forem verdadeiras
# or  -> só retorna FALSE se ambas as condições forem falsas.

# valor boolean
renda_acima_5mil = False
nome_limpo = True

if nome_limpo or renda_acima_5mil == True:
    print('Parabéns, seu financiamento foi aprovado!')
else:
    print('Que pena. Seu financiamento NÃO foi aprovado!')
