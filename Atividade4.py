### Problema
#Verificar se o nível de umidade relativa do ar, informado por um sensor, indica estado crítico de baixa umidade e, em caso positivo, qual deles.

### Entrada
#Um valor inteiro informado pelo sensor como o nível atual da umidade relativa do ar 


umidadear = int(input("Nível de umidade do ar:"))
print("Umidade do ar é: {}%".format(umidadear))

if umidadear >=21 and umidadear <=30:
 print("Estado de Atenção")
elif umidadear >=12 and umidadear <=20: 
 print("Estado de Alerta")
elif umidadear<12:
 print("Estado de Emergência")
else:
 print("Não há perigo")