dias_de_vida = int(input())

mes = (30)
ano = (365)

anos= int(dias_de_vida/ano)
resto_anos = (dias_de_vida%ano)
meses = int(resto_anos/mes)
dias = int(resto_anos%mes)

print(anos,"ano(s)")
print(meses,"mes(es)")
print(dias,"dia(s)")


