""" Ponto do Steak
Criar um programa que dependendo da temperatura do Steak, ele
retorna  o ponto de cozimento. 
O usuário deverá fornecer a temperatura em graus Celsius.

Regra Temperatura:
Menor de 48°C = Cozinhar por mais alguns minutos
48°C = Selada
54°C = Ao ponto para o mal passado
60°C = Ao ponto
65°C = Ao ponto para o bem passado
71°C = Bem passada
Maior 80°C = Está Queimada
"""

temp_carne = int(input('Digite a temperatura da Carne: '))

if temp_carne < 48:
    print('Cozinhar por mais alguns minutos!')
elif temp_carne in range(48, 53):
    print('Selada!')
elif temp_carne in range(54, 59):
    print('Ao ponto para o mal passado!')
elif temp_carne in range(60, 64):
    print('Ao ponto!')
elif temp_carne in range(65, 70):
    print('Ao ponto para o bem passado!')
elif temp_carne in range(71, 79):
    print('Bem passada!')
elif temp_carne >= 80:
    print('A carne está queimada!')
