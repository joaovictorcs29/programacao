print('Exercício 4 - Calcular quantidade de litros de gasolina abastecidos')
print('-------------------------------------------------------------------')

# 1) Ler o preço do litro da gasolina e o valor disponível

valor_litro_gasolina = float(input('Digite o preço do litro da gasolina: R$ ') or "6.87")
valor_disponivel = float(input('Digite o valor disponível para abastecer: R$ '))

# 2) Calcular a quantidade de litros

qtd_litros = valor_disponivel / valor_litro_gasolina

# 3) Exibir o total de litros

print('')
print('O motorista conseguiu colocar', "{:.2f}".format(qtd_litros).replace('.',','), 'litros no tanque.')
