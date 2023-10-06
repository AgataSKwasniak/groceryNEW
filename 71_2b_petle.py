sklep = {"chleb":3.50, "sok":6.00, "woda":1.80, "cukier":4.25}
koszyk = []
while True:
    menu = int(input("1-dodaj produkt do koszyka, 2-pokaz zawartosc koszyka, 3-kasa/koniec"))
    if menu == 1:
        print(sklep)
        produkt = input("Podaj nazwe produktu: ")
        if produkt in sklep:
            koszyk.append(produkt)
        else:
            print("Produkt nie wystepuje w sklepie")
        # produkt moze zosta dodany do koszyka jezeli wystepuje w sklepie winnymn przypadku komunikat blad
    elif menu == 2:
        for x in koszyk:
            print(f"Produkt: {x}")
        #print(koszyk)
        # for x,y in enumerate(koszyk):
        # print(f"Produkt: {x+1}: {y}"))

    elif menu == 3:
        suma = 0
        for x,y in enumerate(koszyk):
            print(f"Produkt {x+1}: {y} Cena: {sklep[y]}")


        suma=suma+ sklep[y]
        print(f"Razem do zaplaty : {suma} PLN")
        break