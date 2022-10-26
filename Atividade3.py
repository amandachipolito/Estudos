### Problema
#Verificar se o nível de umidade relativa do ar, informado por um sensor, indica o nível ideal de umidade do ar para o organismo humano.

### Entrada
#Um valor inteiro informado pelo sensor como o nível atual da umidade relativa do ar 

umidadear = int(input("Nível de umidade do ar:"))
print("Umidade do ar é: {}%".format(umidadear))

if umidadear >=40:
 print("Umidade ideal para o organismo humano")
else:
 print("Abaixo do nível ideal")