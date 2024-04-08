import random

cena = []
zbozi =["CPU","GPU","RAM","HDD","SDD","MotherBorad","Chlazení"]
kos = []



while True:
    print(" ")
    print("1.Dát zboží do košíku")
    print("2.Odebrat zboží z košíku")
    print("3.Zapaltiti obědnávku v košíku")
    volba = int(input("Zvolte vaší možnost: "))    
    
    if volba == 1:
        print(" ")
        for x  in range(len(zbozi)):
            print(f"{x+1}:{zbozi[x]}")

        vyber = input("Vyberte si zboží které chcete do košéku(but číslo pořadí nebo název zboží): ")
        try:
            if 1<= int(vyber) <= len(zbozi):
                kos.append(zbozi[int(vyber)-1])
                zbozi.pop(int(vyber)-1)
            else:
                print("Dali jste špatné zadání")        
        except ValueError:
            if vyber in zbozi:
                kos.append(vyber)
                zbozi.remove(vyber)
            else:
                print("Dali jste špatné zadání")

    elif volba==2:
        if len(kos)>0:    
            print(" ")
            for x  in range(len(kos)):
                print(f"{x+1}:{kos[x]}")

            vyber = input("Vyberte si zboží které chcete odebrat z košéku(but číslo pořadí nebo název zboží): ")
            try:
                if 1<= int(vyber) <= len(kos):
                    zbozi.append(kos[int(vyber)-1])
                    kos.pop(int(vyber)-1)
                else:
                    print("Dali jste špatné zadání")        
            except ValueError:
                if vyber in zbozi:
                    zbozi.append(vyber)
                    kos.remove(vyber)
                else:
                    print("Dali jste špatné zadání")
        else:
            print("košík je prázdný")
    
    
    
    elif volba == 3:
        if len(kos) >0:
            print(" ")
            for x in range(len(kos)):
                a = random.randint(1000,5000)
                print(f"{x}:{kos[x]} za cenu: {a}")
                cena.append(a)
            print(f"Butete muste zaplatit: {sum(cena)} Kč")
            platba = int(input(" chete zaplatit? (Y/N): "))
            if platba == "Y":
                print("Děkujeme za váš nákup")
                break


        
        else:
            print("košík je prázdný")    

             
       