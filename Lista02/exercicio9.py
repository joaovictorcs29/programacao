import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print('Exercício 9 - Ler o valor da compra e escrever o valor total com 10% de desconto')
print('--------------------------------------------------------------------------------')

# 1) Ler a quantidade de cada item da compra

qtd_camisetas = float(input('Digite a quantidade de camisetas compradas: '))
qtd_calcas = float(input('Digite a quantidade de calças compradas: '))
qtd_cintos = float(input('Digite a quantidade de cintos comprados: '))

# 2) Calcular o desconto

# Valores dos produtos
valor_camiseta = 25
valor_calca = 100
valor_cinto = 40

# Valor do desconto
desconto = 0.10

# Cálculo do valor total
valor_total = (qtd_camisetas * valor_camiseta) + (qtd_calcas * valor_calca) + (qtd_cintos * valor_cinto)

# Cálculo do valor do desconto
valor_desconto = valor_total * desconto

# Cálculo do valor total com desconto
valor_total_com_desconto = valor_total - valor_desconto

# 3) Exibir o valor com o desconto em moeda brasileira

print('')
#print('O valor da compra sem desconto é', locale.currency(valor_total, symbol='R$'))
print('O valor do desconto de', str(int(desconto * 100)) + '%', 'é', locale.currency(valor_desconto, grouping=True, symbol='R$'))
print('O valor total da compra com o desconto é', locale.currency(valor_total_com_desconto, grouping=True, symbol='R$'))