### Requisitos
#Para resolver este problema, você deve usar no máximo três comparações básicasNão 
#serão consideradas soluções que utilizem funções prontas para identificação dos valores maiores/menores
#--------------------------------------------------------------------------------------------------------
### Maior
#Dados três valores inteiros, sua tarefa é identificar quem é o maior 
#--------------------------------------------------------------------------------------------------------
### Entrada
#Três linhas, cada uma com um valor inteiro
#--------------------------------------------------------------------------------------------------------
### Saída
#Como nos exemplos
#--------------------------------------------------------------------------------------------------------

variavel1 = int(input("Digite o primeiro número:"))

variavel2 = int(input("Digite o segundo número:"))

variavel3 = int(input("Digite o terceiro número:"))

if variavel1>(variavel2 and variavel3):
    print("O primeiro número é o maior")
else:
    if variavel3>(variavel1 and variavel2):
        print("O terceiro número é o maior")
    else: 
        print("O segundo número é o maior")