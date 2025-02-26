### 8. **Contador de Vogais em uma String**
   #Peça ao usuário para digitar uma palavra ou frase.
    #Conte quantas vogais (a, e, i, o, u) existem na string.
    #Exiba o resultado na tela.
print('Contador de vogais em texto')

#construindo a funçao de contagem de vogais
def contar_vogais(texto):
    return sum(1 for vogal in texto if vogal in "aeiouAEIOU")
    
#Solicitando ao usuario que digite um texto ou palavra
texto = input('Digite um texto ou palavra: ')
    
#chamando a funçao de contar vogais
qtd_vogais = contar_vogais(texto)
print(f'O texto "{texto}" contem {qtd_vogais} vogais')