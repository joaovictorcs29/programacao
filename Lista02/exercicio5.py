print('Exercício 5 - Calcular média final')
print('----------------------------------')

# 1) Ler a nota do grau A e do grau B

nota_grau_a = float(input('Digite a nota do grau a: '))
nota_grau_b = float(input('Digite a nota do grau b: '))

# Pesos das graus

peso_grau_a = 1/3
peso_grau_b = 2/3

# 2) Calcular a média

media_final = (nota_grau_a * peso_grau_a) + (nota_grau_b * peso_grau_b)

# 3) Exibir a média final

print('')
print('Sua média final arredondada é', round(media_final, 2))
