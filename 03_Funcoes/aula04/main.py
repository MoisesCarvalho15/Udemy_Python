# Argumentos xargs com números
# Tarefa: Criar um programa que some vários números

def soma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    
    return resultado

exemplo1 = soma(2, 3, 4, 5)
exemplo2 = soma(10, 20, 30, 40, 50)

print(f'Exemplo 1: {exemplo1}')
print(f'Exemplo 2: {exemplo2}')
