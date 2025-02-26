#Calculadora aritimética
try:
	x  = float(input('Digite o primeiro número: '))
	y  = float(input('Digite o segundo número: '))
	z  = float(input('Digite o terceiro número: '))

#cálculo da média aritimética
	media = (x + y +z)/3

#Exibição dos dados de saída
	print(f'A média dos tres valores é:  {media}')
except ValueError:
	print(f'Erro: Por favor, digite apenas números')
	

