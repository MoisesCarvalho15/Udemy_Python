# While loop

valor_produto = 100
dia_de_venda = 0

while valor_produto > 20:
    dia_de_venda += 1
    print(f'No dia {dia_de_venda} produto vendido no valor de R${valor_produto:.2f}')
    valor_produto -= 5
