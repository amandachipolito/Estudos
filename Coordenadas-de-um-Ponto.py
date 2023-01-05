x,y = map(float,input().split())

origem = (x==0 and y==0)

q1 = (x>origem and y>origem) 
q2 = (x<origem and y>origem)
q3 = (x<origem and y<origem)
q4 = (x>origem and y<origem)

eixox = (x==0)
eixoy = (y==0)


if origem:
    print("Origem")
elif eixox:
    print("Eixo Y")   
elif eixoy:
    print("Eixo X")
elif q1:
    print("Q1")
elif q2:
    print("Q2")
elif q3:
    print("Q3")
else:
    if q4:
     print("Q4")


