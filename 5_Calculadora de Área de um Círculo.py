# Calculadora de Área de um Círculo**
#   - Peça ao usuário para digitar o raio de um círculo.
#   - Calcule a área usando a fórmula: `área = π * raio²` (use `π = 3.14159`).
#   - Exiba o resultado na tela.

#importa o pacote de funções matemáticas


#Abre o programa e verifica se o dado raio é um número
print('Calculadora de área de um círculo')
try:
	raio = float(input('Digite o raio do círculo: '))
	
	#verifica se o raio é negativo 
	if raio <= 0:
		print('Erro: o raio não pode ter valor nulo ou negativo.')
	else:
		area = 3.14159 * (raio ** 2)

		#exibe resultado da área calculada 
		print(f'A área do círculo de raio {raio:.2f} é de {area:.2f}')

#tratamento do Erro da Entrada de dado
except ValueError:
	print('Erro. O valor do raio não é válido')
