#### Bela idade
#Seu programa deve ler a idade de uma aluna e dar uma mensagem apropriada
#- a partir de 60, é a melhor idade
#- entre 18 e 59, é a maioridade
#- antes dos 18, é a tenra idade

### Entrada
#Um valor inteiro


idade = int(input("Idade da Aluna:"))

if idade <18:
    print("Tenra idade")
elif idade >=18 and idade<59:
    print("Maioridade")
else:
    print("Melhor idade")    