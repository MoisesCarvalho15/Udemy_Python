""" Calculadora para Pintura
Criar um programa que calcule a quantidade de tinta necessária
para pintar uma parede.
O usuário deverá fornecer as seguintes informações:
* Rendimento
* altura
* largura
Ao final exibir a mensagem: 'Você precisa de X latas de tinta'
"""

rendimento = int(input('Digite o RENDIMENTO da lata: '))
largura = float(input('Digite a LARGURA da parede: '))
altura = float(input('Digite a ALTURA da parede: '))

qnt_latas = (largura * altura) / rendimento

print(f'Você precisa de {qnt_latas:.2f} latas de tinta')
