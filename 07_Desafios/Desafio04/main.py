"""Calculadora de IMC
Criar um programa que solicite as seguintes informações:
* Altura
* Peso

Tabela de Índice de Massa Corporal (IMC)
# Menor que 18,5 MAGREZA
# Entre 18,5 e 24,9 NORMAL
# Entre 25,0 e 29,9 SOBREPESO
# Entre 30,0 e 39,9 OBESIDADE
# Maior que 40,0    OBESIDADE GRAVE
"""

altura = float(input('Digite sua altura em cm: '))
peso = float(input('Digite seu peso: '))

imc = peso / (altura/100) **2

if imc < 18.5:
    print(f'{imc:.2f} | MAGREZA')
elif imc >= 18.5 and imc < 24.99:
    print(f'{imc:.2f} | NORMAL')
elif imc >= 25 and imc < 29.99 :
    print(f'{imc:.2f} | SOBREPESO')
elif imc >= 30 and imc < 39.99:
    print(f'{imc:.2f} | OBESIDADE')
elif imc >= 40:
    print(f'{imc:.2f} | OBESIDADE GRAVE')
