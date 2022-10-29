###    #ATENÇÃO: Requisito    #### 
#Você pode utilizar no máximo 4 comparações
#Note que essa verificação é manual! mesmo com 'accepted' no beecrowd, sua solução só vai ser
# aceita pela professora se atender o requisito especificado! 8-o
#--------------------------------------------------------------------------------------------
### Mais velha entre 4 irmãs
#Dadas das idades de quatro irmãs, quem é a mais velha?
#--------------------------------------------------------------------------------------------
### Requisito
#Você pode utilizar no máximo 4 comparações
#--------------------------------------------------------------------------------------------
### Entrada
#Quadro linhas, cada uma com uma idade
#--------------------------------------------------------------------------------------------
### Saída
#Como nos exemplos
#--------------------------------------------------------------------------------------------

idade1 = int(input("Idade da primeira irmã:"))

idade2 = int(input("Idade da segunda irmã:"))

idade3 = int(input("Idade da terceira irmã:"))

idade4 = int(input("Idade da quarta irmã:"))

if idade1>(idade2 and idade3 and idade4):
    print(("A irmã mais velha tem {} anos").format(idade1))
else:
    if idade2>(idade1 and idade3 and idade4):
        print(("A irmã mais velha tem {} anos").format(idade2))
    else:
        if idade3>(idade1 and idade2 and idade4):
            print(("A irmã mais velha tem {} anos").format(idade3))
        else:
            idade4>(idade1 and idade2 and idade3)
            print(("A irmã mais velha tem {} anos").format(idade4))
        