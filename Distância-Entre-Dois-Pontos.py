xy1 = input().split()
xy2 = input().split()

lista1 = [float(i) for i in xy1]
lista2 = [float(i) for i in xy2]

x = (lista2[0]-lista1[0])**2
y = (lista2[1]-lista1[1])**2

soma = x+y

raiz = float(soma)**0.5

print("{:.4f}".format(raiz))