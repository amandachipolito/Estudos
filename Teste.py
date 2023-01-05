n1,n2,n3,n4 = map(float,input().split(' '))

n1 = n1*2/10
n2 = n2*3/10
n3 = n3*4/10
n4 = n4*1/10

soma = (n1+n2+n3+n4)

print("Media: {:.1f}".format(round(soma,2)))

if soma>=7.0:
    print("Aluno aprovado.")
else:
    if soma>=5.0 and soma<7.0:
     print("Aluno em exame.")
     n5 = float(input())
     print("Nota do exame: {:.1f}".format(n5))
     soma = (soma+n5)/2
     if soma>=5.0:
        print("Aluno aprovado.")
        print("Media final: {:.1f}".format(round(soma,2)))
     else:
        print("Aluno reprovado.")
    else:
        if soma<5.0:
            print("Aluno reprovado.")
        


