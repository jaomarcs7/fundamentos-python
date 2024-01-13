nome = 'João Marcos'
altura = 1.80
peso = 95 
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

"f-strings"
print(linha_1)
print('pesa',  peso, 'quilos e seu IMC é',)
print(imc)
 
# João Marcos tem 1.80 de altura,
# Pesa 95 quilos e seu IMC é 