qualquer = float(input())

if qualquer >= 0 and qualquer <= 25:
    print("Intervalo [0,25]")
elif qualquer > 25  and qualquer <= 50:
    print("Intervalo (25,50]")
elif qualquer > 50 and qualquer <= 75:
    print("Intervalo (50,75]")
elif qualquer > 75 and qualquer <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")