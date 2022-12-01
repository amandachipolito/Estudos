lista = input().split()

lista1 = [float(i) for i in lista]

a = lista1[0]
b = lista1[1]
c = lista1[2]

area_triangulo = (a*c)/2
area_circulo = (3.14159 * c**2)
area_trapezio = ((a+b)*c)/2
area_quadrado = b**2
area_retangulo = a*b

print("TRIANGULO: {:.3f}".format(area_triangulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapezio))
print("QUADRADO: {:.3f}".format(area_quadrado))
print("RETANGULO: {:.3f}".format(area_retangulo))