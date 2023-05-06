"""
* For loop - Utilizando if and else

* Enviar um email com os detalhes da compra online
* Máximo de 3 tentativas para compras confirmadas.
"""

compra_confirmada = False
dados_compra = 'Compra realizada no valor de R$26,50 e entrega confirmada.'


for enviar in range(3):
    if compra_confirmada == True:
        print(dados_compra)
        print('Detalhes enviados para o email cadastrado.')
        break # saindo do for loop
    else:
        print('Compra não foi realizada!')
        break # saindo do for loop
