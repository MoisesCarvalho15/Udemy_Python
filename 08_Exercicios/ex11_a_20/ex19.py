"""
Crie um programa onde o usuário deverá adivinhar o nome da fruta.
Enquanto a fruta não for acertada, o programa deverá ficar
solicitando o nome da fruta.
Caso seja acertada o nome, imprima: "Parabéns, você acertou a fruta!"
"""


while True: 
    fruta = input('Digite o nome de uma fruta: ').lower()
    
    if fruta == 'manga':
        print('Parabéns! Você acertou a fruta.')
        break
    else:
        print('Você errou!')
