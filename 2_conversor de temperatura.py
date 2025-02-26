
#Solicitando entrada de dados e verificando valore numerico
try:
	tempC = float(input('Digite o valor em graus Celsius: '))
	
	# Verificação de temperatura abaixo do zero absoluto
    if tempC < -273.15:
        print("Erro: Temperatura abaixo do zero absoluto (-273,15°C) é fisicamente impossível.")
    else:
	
	#conversão de Celsius para Fahrenheit 
	tempF = (tempC *9/5) + 32
	
	#exibição do valor convertido
	print(f'A temperatura de {tempC:.2f}° Celsius, equivale a {tempF:.2f}° Fahrenheit')
	#verificação de erro
except ValueError:
	print('Erro: digite apenas números.')