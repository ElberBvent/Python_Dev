print('Verificador de número par oi impar')

#verificando se o dado de entrada é um número
try:
	num = int(input('Digite um número inteiro: '))
	
	#checando se é par ou impar e exibindo resultado
	if num % 2 == 0:
		print(f'O número {num} é PAR')
	else:
		print(f'O número {num} é IMPAR')
		
#verificando se o usuário digitou um número

except ValueError:
		print('Erro. Não foi digitado um número válido. ')
		