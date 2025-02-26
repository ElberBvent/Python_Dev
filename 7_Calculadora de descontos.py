# 7. **Calculadora de Desconto
#Peça ao usuário para digitar o valor de um produto e a porcentagem de desconto
#Calcule o valor final do produto após o desconto.
#Exiba o resultado na tela.
print=('Calculadora de descontos')

try:
    # pedir pra digitar um valor e a porcentagem do descontos
   valor = float(input('Digite o valor do produto: '))
   porcentual = int(input('Digite o porcentual de desconto: '))
   
   #calculo do desconto
   desconto = valor * (porcentual / 100)
   
   #Exibe o valor Calculadora
   print(f'O valor final do produto eh: {desconto}.')
   
except ValueError:
    print('Erro. Nao foram digitados valores validos')