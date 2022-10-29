### O que seu programa deve fazer?
#Seu programa deve checar se os documentos apresentados por uma pessoa estão completos ou não


### Entrada
#Primeira linha:  F ou M, indicando sexo feminino ou masculino

sexo = str(input("F para feminino ou M para masculino:"))


#####

rg = int(input("Insira seu RG:")) #Segunda linha: S ou N, para primeiro documento apresentado corretamente ou não 
if rg!=0:
    tituloeleitor = int(input("Insira seu título de eleitor:")) #Terceira linha:   S ou N, para segundo documento apresentado corretamente  ou não 
    print(sexo)
    if rg>0: 
        print("S")
        if tituloeleitor!=0: 
            print("S")
            #Quarta linha: S ou N, para terceiro documento apresentado corretamente ou não
            #A quarta linha é fornecida apenas no caso de pessoa do sexo masculino 
            if sexo == "m":
                reservista = input("Número da Reservista:")
                if reservista == '':
                    print("Incompleto")

                if reservista==0:
                    print("Incompleto")
                else:
                        if reservista>"1":
                            print("completo")

            if sexo == "M":
                reservista = input("Número da Reservista:")
                if reservista == '':
                    print("Incompleto")

                if reservista==0:
                    print("Incompleto")
                else:
                        if reservista>"1":
                            print("completo")

            if sexo == str("f"):
                    print("Completo") 

            if sexo == str("F"):
                    print("Completo")         
        else:    
            print("N")
    else:
     print("N")    

## tive que copiar várias vezes o if para reservista porque meu código não aceitava as condições de "m" ou "M". Perguntar à professora
## como posso resolver esse problema para não ter que ficar adicionando tantas linhas de código desnecessárias
 