import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print('Exercício 3 - Calcular quanto o dono da padaria arrecadou com a venda de pães e broas')
print('-------------------------------------------------------------------------------------')

# 1) Ler quanto vendeu de pães e broas

qtd_paes = int(input('Digite o total de pães vendidos: '))
qtd_broas = int(input('Digite o total de broas vendidas: '))

# 2) Calcular a venda

# Valores dos produtos
valor_do_pao = 0.5
valor_da_broa = 2

# Cálculo das vendas
venda_paes = qtd_paes * valor_do_pao
venda_broas = qtd_broas * valor_da_broa
venda_total = venda_paes + venda_broas

# 3) Exibir o resultado em moeda brasileira

print('')
print('Valor do pão:', locale.currency(valor_do_pao, grouping=True, symbol='R$'))
print('Total de pães:', locale.currency(venda_paes, grouping=True, symbol='R$'), '\n')

print('Valor da broa:', locale.currency(valor_da_broa, grouping=True, symbol='R$'))
print('Total de broas:', locale.currency(venda_broas, grouping=True, symbol='R$'), '\n')

print('Total arrecadado:', locale.currency(venda_total, grouping=True, symbol='R$'))
