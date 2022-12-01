a = input().split()
b = input().split()

lista1 = [float(i) for i in a]
lista2 = [float(i) for i in b]

c = lista1[1]*lista1[2]
d = lista2[1]*lista2[2]

e = c+d

print("VALOR A PAGAR: R$ {:.2f}".format(e))