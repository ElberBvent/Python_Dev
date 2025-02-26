#Gerador de Tabuada
#Peça ao usuário para digitar um número inteiro.
#Exiba a tabuada desse número de 1 a 10.

try:
    # TODO: write code...
    #Pedindo para o usuario digitar um numero inteiro
    numero = int(input('Digite um numero inteiro para gerar a tabuada: '))
    multiplicador = [1,2,3,4,5,6,7,8,9,10]
    
    #Validando se o numero eh inteiro
    if numero <= 0:
        print('ERRO. Por favor, digite um numero inteiro maior que zero')
    else:
        for valor in multiplicador:
            resultado = numero * valor
            print(f'{numero} x {valor} = {resultado}')
            
    
except ValueError:
    print('Erro. Por favor, digite um numero inteiro.')