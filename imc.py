nome = input('Qual é seu nome?')
altura = float(input('Qual é sua altura?'))
peso = int(input( 'Qual é seu peso'))
imc = peso / (altura ** 2)

print(f'{nome} tem {altura:.2f} de altura')
print(f'pesa {peso} kilos e seu imc é {imc}')


