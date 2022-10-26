### O que o seu programa tem que fazer?
# Usar as equivalências acima para apresentar em mililitros os valores 
# das receitas que você e outras pessoas vão usar na creche

### Entrada
# Três linhas: números de xícaras da receita; números de colheres de 
# sopa da receita, números de colheres da chá da receita
# Nota: se uma receita não utilizar alguma das medidas, o valor 
# correspondente é dado como 0 (zero)

### Saída
#O volume equivalente em ml para cada uma das porções necessárias 
# à receita, como nos exemplos

mlxic = int(240)

mlsop = int(15)

mlcha = int(5)

xicara = int(input("Quantas xícaras tem sua receita?:"))*mlxic

colhers = int(input("Quantas colheres de sopa tem sua receita?:"))*mlsop

colherc = int(input("Quantas colheres de chá tem sua receita?:"))*mlcha

print("Receita é {}ml do ingrediente 1, {}ml do ingrediente 2 e {}ml do ingrediente 3".format(xicara, colhers, colherc))