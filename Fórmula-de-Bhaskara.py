a,b,c = map(float,input().split())

if a>0:
    delta = (b**2)-(4*a*c)
    if delta>0:

        x1 = (-b+delta**0.5) / (2*a)
        x2 = (-b-delta**0.5) / (2*a)

        print('R1 = {:.5f}'.format(x1))
        print('R2 = {:.5f}'.format(x2))
    else:
        print("Impossivel calcular")
else:
    print("Impossivel calcular")

