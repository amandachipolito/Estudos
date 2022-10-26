### Problema
#Verificar se o nível de umidade relativa do ar, informado por um sensor, indica uma situação de alerta para o organismo humano.

### Entrada
#Um valor inteiro informado pelo sensor como o nível atual da umidade relativa do ar 

### Saída
#Como nos exemplos

umidadear = int(input("Nível de umidade do ar:"))
print("Umidade do ar é: {}%".format(umidadear))

if umidadear <=30:
 print("Perigo")
elif umidadear >=31 and umidadear <=40: 
 print("Alerta")
else:
 print("Não há perigo")