#Verificador de Número Positivo, Negativo ou Zero**
#Peça ao usuário para digitar um número.
#Verifique se o número é positivo, negativo ou zero e exiba a mensagem correspondente.

#Validando os dados de entrada
try:
    #Solicitando ao usuario que digite um numero
    numero = int(input('Digite um numero inteiro: '))
    
    #Verificando se o numero eh positivo, negativo ou zero, e exibindo resultado
    if numero < 0:
        print(f'{numero} eh negativo')
    elif numero > 0:
        print(f'{numero} eh positivo')
    else:
        print(f'{numero} eh zero')
    
except ValueError:
    print('Erro. Nao foi digitado um numero')
    