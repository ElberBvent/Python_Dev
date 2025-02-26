#Calculadora de Juros simples
#Peça ao usuário para digitar o valor principal, a taxa de juros (em porcentagem) e o tempo (em anos).
#Calcule o juros simples usando a fórmula: `juros = (principal * taxa * tempo) / 100`.
#Exiba o resultado na tela

#Soiicitando os dados ao usuario
try:
    
    valorPrincipal = float(input('Digite o valor principal: '))
    taxaJuros = float(input('Digite a taxa de juros em porcentagem: '))
    tempo = float(input('Digite o tempo em anos: '))
    
    # Validando se todos os valores sao positivos
    if valorPrincipal < 0 or taxaJuros < 0 or tempo < 0:
        print('Erro. Todos os valores devem ser positivos.')
    else:

       	#calculando os juros simples
       	 juros = (valorPrincipal * taxaJuros * tempo) / 100

        	#Exibindo resultado
       	 print(f'Os juros para o valor de {valorPrincipal}, no periodo de {tempo} anos eh de: {juros:.2f}')
except ValueError:
    print('Erro. Por favor, digite valores numericos positivos')
