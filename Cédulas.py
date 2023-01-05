v = int(input())

if 0 < v < 1000000:
    restocem = v%100
    dividendo100 = v//100
    print(v)
    print(dividendo100, "nota(s) de R$ 100,00")
    restocinquenta = restocem%50
    dividendo50 = restocem//50
    print(dividendo50, "nota(s) de R$ 50,00")
    resto20 = restocinquenta%20
    dividendo20 = restocinquenta//20
    print(dividendo20, "nota(s) de R$ 20,00")
    resto10 = resto20%10
    dividendo10 = resto20//10
    print(dividendo10, "nota(s) de R$ 10,00")
    resto5 = resto10%5
    dividendo5 = resto10//5
    print(dividendo5, "nota(s) de R$ 5,00")
    resto2 = resto5%2
    dividendo2 = resto5//2
    print(dividendo2, "nota(s) de R$ 2,00")
    resto1 = resto2%1
    dividendo1 = resto2//1
    print(dividendo1, "nota(s) de R$ 1,00")
    

