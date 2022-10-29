### Requisito
#Para resolver este problema, você deve usar no máximo uma comparação básica (apenas um if-else)
#Não serão consideradas soluções que utilizem funções prontas para identificação dos valores maiores/menores
#------------------------------------------------------------------------------------------------------------
### Maior e Menor
#Dados dois valores inteiros, sua tarefa é identificar quem é o maior e quem é o menor
#------------------------------------------------------------------------------------------------------------
### Entrada
#Duas linhas, cada uma com um valor inteiro
#------------------------------------------------------------------------------------------------------------
#Saída
#Como nos exemplos
#------------------------------------------------------------------------------------------------------------

variavel1 = int(input("Escreva o primeiro número:"))
variavel2 = int(input("Escreva o segundo número:"))

if variavel1 >variavel2:
    print(("Maior: {} - o primeiro número escrito").format(variavel1))
else:
    print(("Maior: {} - o segundo número escrito").format(variavel2))
