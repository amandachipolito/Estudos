lanches = ["Cachorro Quente", "X-Salada", "X-Bacon", "Torrada simples", "Refrigerante"]
valores = [4.00, 4.50, 5.00, 2.00, 1.50]

insira = map(int, input().split())

insira = list(insira)

if insira[0] == 1:
    quantidade = int(insira[1]) * valores[0]
elif insira[0] == 2:
    quantidade = int(insira[1]) * valores[1]
elif insira[0] == 3:
    quantidade = int(insira[1]) * valores[2]
elif insira[0] == 4:
    quantidade = int(insira[1]) * valores[3]
elif insira[0] == 5:
    quantidade = int(insira[1]) * valores[4]

print("Total: R$ {:.2f}".format(quantidade))
