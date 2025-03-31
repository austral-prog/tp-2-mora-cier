def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)

    print(f"\nVuelto") 

    print(f"\nPesos:")
    vuelto = money - expense
    pesos = int(vuelto)
    print(pesos)

    print("Centavos:")
    centavos = int((vuelto - pesos) * 100)
    print(centavos)
