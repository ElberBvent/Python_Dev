# 6. **Soma de Números Pares em um Intervalo**

print('Soma de Números Pares em um Intervalo')

#   - Peça ao usuário para digitar dois números inteiros (início e fim de um intervalo).
try:
	startRange = int(input('Digite um número inteiro para o início do intervalo: '))
	stopRange = int(input('Digite um número inteiro para o fim do intervalo: '))
	intervalo = [startRange, stopRange]

	#   - Calcule a soma de todos os números pares nesse intervalo.
	somaPares = 0
	for i in range(startRange, stopRange +1):
		if i % 2 == 0:
			somaPares += i

		
	#   - Exiba o resultado na tela.
	print(F'A soma dos números Pares entre {startRange} e {stopRange}, é: {somaPares}')

#captura Erro de digitação de intervalo não numérico
except ValueError:
	print('Erro. O valor digitado para o intervalo, não é numérico')

