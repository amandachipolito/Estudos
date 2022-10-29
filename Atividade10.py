### Primeiro nome, nome do meio, sobrenome
#Seu programa deve ler três linhas, cada uma com uma parte do nome, e imprimir o nome completo.
#Caso não exista nome do meio, e entrada correspondente é indicada com um ponto final.
#-------------------------------------------------------------------------------------------------
### Entrada
#Primeira linha: primeiro nome
#Segunda linha: nome do meio (ou ponto final)
#Terceira linha: sobrenome
#-------------------------------------------------------------------------------------------------
### Saída
#Nome completo
#-------------------------------------------------------------------------------------------------

nome = str(input("Nome: "))
meio = str(input("Nome do Meio (caso não tenha, coloque ponto final): "))
sobrenome = str(input("Sobrenome: "))

if meio==".":
    print(nome,sobrenome)
else:
    print(nome,meio,sobrenome)