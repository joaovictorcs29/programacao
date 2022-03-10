import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print('Exercício 8 - Ler o valor da compra e escrever o valor com 15% de desconto')
print('--------------------------------------------------------------------------')

# 1) Ler o valor da compra

valor_da_compra = float(input('Digite o valor da compra: '))

# 2) Calcular o desconto

# Valor do desconto
desconto = 0.15

# Cálculo do desconto
valor_com_desconto = valor_da_compra - (valor_da_compra * desconto)

# 3) Exibir o valor com o desconto em moeda brasileira

print('')
print('O valor da compra com o desconto de', str(int(desconto * 100)) + '%' , 'é', locale.currency(valor_com_desconto, grouping=True, symbol='R$'))
