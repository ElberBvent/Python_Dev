#verifica validade dos valores de entrada
try:
	print('Calculadora de IMC')
	altura = float(input('Digite a altura em metros: '))
	peso = float(input('Digite o peso em kg: '))
	
	#verifica valores impossíveis
	if altura <= 0 or peso <= 0:
		print('Erro: altura e peso devem ter valores maiores que 0.')
	else:
		
		#calcula IMC: peso / (altura ** 2)
		imc = peso / (altura ** 2)
		
		#exibe os resultados no
		print(f'O valor do IMC calculado é de: {imc:.2f} ')
	
#captura erros de entrada nao numerica
except ValueError:
		print('Erro: Os valores de peso e altura devem ser numéricos')
		
	