print(" ")
print("Hledani min")

import random

import time
time.sleep(3)
print("Pro výhraní hry musíte položit vlaječky na všechny miny")
time.sleep(3)
print("Velejček můžete položit max 7")
time.sleep(3)
print("Ve hře se muže vyskytovat 3 až 7 min")
time.sleep(3)
print("Hodně štestí(Hra zachvíli začne)")
time.sleep(5)



A1 = " "
A2 = " "
A3 = " "
A4 = " "
A5 = " "
B1 = " "
B2 = " "
B3 = " "
B4 = " "
B5 = " "
C1 = " "
C2 = " "
C3 = " "
C4 = " "
C5 = " "
D1 = " "
D2 = " "
D3 = " "
D4 = " "
D5 = " "
E1 = " "
E2 = " "
E3 = " "
E4 = " "
E5 = " "

pole = [A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5,E1,E2,E3,E4,E5]

bomba = []
konec = False

radek = ["A","B","C","D","E"]
sloupec = [1,2,3,4,5]

def Vybranepole(vybrano):
    global A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5,E1,E2,E3,E4,E5

    if vybrano == "A1":
        A1 = A1save
    elif vybrano == "A2":
        A2 = A2save
    elif vybrano == "A3":
        A3 = A3save
    elif vybrano == "A4":
        A4 = A4save
    elif vybrano == "A5":
        A5 = A5save
    elif vybrano == "B1":
        B1 = B1save
    elif vybrano == "B2":
        B2 = B2save
    elif vybrano == "B3":
        B3 = B3save
    elif vybrano == "B4":
        B4 = B4save
    elif vybrano == "B5":
        B5 = B5save
    elif vybrano == "C1":
        C1 = C1save
    elif vybrano == "C2":
        C2 = C2save
    elif vybrano == "C3":
        C3 = C3save
    elif vybrano == "C4":
        C4 = C4save
    elif vybrano == "C5":
        C5 = C5save
    elif vybrano == "D1":
        D1 = D1save
    elif vybrano == "D2":
        D2 = D2save
    elif vybrano == "D3":
        D3 = D3save
    elif vybrano == "D4":
        D4 = D4save
    elif vybrano == "D5":
        D5 = D5save
    elif vybrano == "E1":
        E1 = E1save
    elif vybrano == "E2":
        E2 = E2save
    elif vybrano == "E3":
        E3 = E3save
    elif vybrano == "E4":
        E4 = E4save
    elif vybrano == "E5":
        E5 = E5save

def Kontorlamin(vybrano):
    global A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5,E1,E2,E3,E4,E5
    if vybrano in bomba:
        if "A1" in bomba:
            A1 = "¤"
        if "A2" in bomba:
            A2 = "¤"
        if "A3" in bomba:
            A3 = "¤"
        if "A4" in bomba:
            A4 = "¤"
        if "A5" in bomba:
            A5 = "¤"

        if "B1" in bomba:
            B1 = "¤"
        if "B2" in bomba:
            B2 = "¤"
        if "B3" in bomba:
            B3 = "¤"
        if "B4" in bomba:
            B4 = "¤"
        if "B5" in bomba:
            B5 = "¤"

        if "C1" in bomba:
            C1 = "¤"
        if "C2" in bomba:
            C2 = "¤"
        if "C3" in bomba:
            C3 = "¤"
        if "C4" in bomba:
            C4 = "¤"
        if "C5" in bomba:
            C5 = "¤"

        if "D1" in bomba:
            D1 = "¤"
        if "D2" in bomba:
            D2 = "¤"
        if "D3" in bomba:
            D3 = "¤"
        if "D4" in bomba:
            D4 = "¤"
        if "D5" in bomba:
            D5 = "¤"

        if "E1" in bomba:
            E1 = "¤"
        if "E2" in bomba:
            E2 = "¤"
        if "E3" in bomba:
            E3 = "¤"
        if "E4" in bomba:
            E4 = "¤"
        if "E5" in bomba:
            E5 = "¤"
        
        Pole()
        print("Šlápli jste na minu prohrál jste, niní se ukažou všehcny miny.") 
        return True

def Vlajecky(vybrano):
    global A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5,E1,E2,E3,E4,E5
    
    if vybrano == "A1":
        A1 = "♦"
    elif vybrano == "A2":
        A2 = "♦"
    elif vybrano == "A3":
        A3 = "♦"
    elif vybrano == "A4":
        A4 = "♦"
    elif vybrano == "A5":
        A5 = "♦"
    elif vybrano == "B1":
        B1 = "♦"
    elif vybrano == "B2":
        B2 = "♦"
    elif vybrano == "B3":
        B3 = "♦"
    elif vybrano == "B4":
        B4 = "♦"
    elif vybrano == "B5":
        B5 = "♦"
    elif vybrano == "C1":
        C1 = "♦"
    elif vybrano == "C2":
        C2 = "♦"
    elif vybrano == "C3":
        C3 = "♦"
    elif vybrano == "C4":
        C4 = "♦"
    elif vybrano == "C5":
        C5 = "♦"
    elif vybrano == "D1":
        D1 = "♦"
    elif vybrano == "D2":
        D2 = "♦"
    elif vybrano == "D3":
        D3 = "♦"
    elif vybrano == "D4":
        D4 = "♦"
    elif vybrano == "D5":
        D5 = "♦"
    elif vybrano == "E1":
        E1 = "♦"
    elif vybrano == "E2":
        E2 = "♦"
    elif vybrano == "E3":
        E3 = "♦"
    elif vybrano == "E4":
        E4 = "♦"
    elif vybrano == "E5":
        E5 = "♦"

def VylejckaRemove(vybrano):
    global A1,A2,A3,A4,A5,B1,B2,B3,B4,B5,C1,C2,C3,C4,C5,D1,D2,D3,D4,D5,E1,E2,E3,E4
    if vybrano == "A1":
        A1 = " "
    elif vybrano == "A2":
        A2 = " "
    elif vybrano == "A3":
        A3 = " "
    elif vybrano == "A4":
        A4 = " "
    elif vybrano == "A5":
        A5 = " "
    elif vybrano == "B1":
        B1 = " "
    elif vybrano == "B2":
        B2 = " "
    elif vybrano == "B3":
        B3 = " "
    elif vybrano == "B4":
        B4 = " "
    elif vybrano == "B5":
        B5 = " "
    elif vybrano == "C1":
        C1 = " "
    elif vybrano == "C2":
        C2 = " "
    elif vybrano == "C3":
        C3 = " "
    elif vybrano == "C4":
        C4 = " "
    elif vybrano == "C5":
        C5 = " "
    elif vybrano == "D1":
        D1 = " "
    elif vybrano == "D2":
        D2 = " "
    elif vybrano == "D3":
        D3 = " "
    elif vybrano == "D4":
        D4 = " "
    elif vybrano == "D5":
        D5 = " "
    elif vybrano == "E1":
        E1 = " "
    elif vybrano == "E2":
        E2 = " "
    elif vybrano == "E3":
        E3 = " "
    elif vybrano == "E4":
        E4 = " "
    elif vybrano == "E5":
        E5 = " "


def Pripravahry():
    global pocet, vybrano, bomba,A1save, A2save, A3save, A4save, A5save, B1save, B2save, B3save, B4save, B5save, C1save, C2save, C3save, C4save, C5save, D1save, D2save, D3save, D4save, D5save, E1save, E2save, E3save, E4save, E5save
    
    A1save = 0
    A2save = 0
    A3save = 0
    A4save = 0
    A5save = 0
    B1save = 0
    B2save = 0
    B3save = 0
    B4save = 0
    B5save = 0
    C1save = 0
    C2save = 0
    C3save = 0
    C4save = 0
    C5save = 0
    D1save = 0
    D2save = 0
    D3save = 0
    D4save = 0
    D5save = 0
    E1save = 0
    E2save = 0
    E3save = 0
    E4save = 0
    E5save = 0
    
    bomba = []
    pocet = random.randint(3,7)
    for i in range(pocet):
        moznosti = ["A1", "A2", "A3", "A4", "A5", "B1", "B2", "B3", "B4", "B5", "C1", "C2", "C3", "C4", "C5", "D1", "D2", "D3", "D4", "D5", "E1", "E2", "E3", "E4", "E5"]
        vybrano = random.choice(moznosti)
        moznosti.remove(vybrano)
        bomba.append(vybrano)
        if vybrano == "A1":
            A1save = "¤"
        elif vybrano == "A2":
            A2save = "¤"
        elif vybrano == "A3":
            A3save = "¤"
        elif vybrano == "A4":
            A4save = "¤"
        elif vybrano == "A5":
            A5save = "¤"
        elif vybrano == "B1":
            B1save = "¤"
        elif vybrano == "B2":
            B2save = "¤"
        elif vybrano == "B3":
            B3save = "¤"
        elif vybrano == "B4":
            B4save = "¤"
        elif vybrano == "B5":
            B5save = "¤"
        elif vybrano == "C1":
            C1save = "¤"
        elif vybrano == "C2":
            C2save = "¤"
        elif vybrano == "C3":
            C3save = "¤"
        elif vybrano == "C4":
            C4save = "¤"
        elif vybrano == "C5":
            C5save = "¤"
        elif vybrano == "D1":
            D1save = "¤"
        elif vybrano == "D2":
            D2save = "¤"
        elif vybrano == "D3":
            D3save = "¤"
        elif vybrano == "D4":
            D4save = "¤"
        elif vybrano == "D5":
            D5save = "¤"
        elif vybrano == "E1":
            E1save = "¤"
        elif vybrano == "E2":
            E2save = "¤"
        elif vybrano == "E3":
            E3save = "¤"
        elif vybrano == "E4":
            E4save = "¤"
        elif vybrano == "E5":
            E5save = "¤"
    
    if "A1" in bomba:
        if A2save != "¤":
            A2save += 1
        if B1save != "¤":
            B1save += 1
        if B2save != "¤":
            B2save += 1

    if "A2" in bomba:
        if A1save != "¤":
            A1save += 1
        if A3save != "¤":
            A3save += 1
        if B1save != "¤":
            B1save += 1
        if B2save != "¤":
            B2save += 1
        if B3save != "¤":
            B3save += 1

    if "A3" in bomba:
        if A2save != "¤":
            A2save += 1
        if A4save != "¤":
            A4save += 1
        if B2save != "¤":
            B2save += 1
        if B3save != "¤":
            B3save += 1
        if B4save != "¤":
            B4save += 1

    if "A4" in bomba:
        if A3save != "¤":
            A3save += 1
        if A5save != "¤":
            A5save += 1
        if B3save != "¤":
            B3save += 1
        if B4save != "¤":
            B4save += 1
        if B5save != "¤":
            B5save += 1

    if "A5" in bomba:
        if A4save != "¤":
            A4save += 1
        if B4save != "¤":
            B4save += 1
        if B5save != "¤":
            B5save += 1

    if "B1" in bomba:
        if A1save != "¤":
            A1save += 1
        if A2save != "¤":
            A2save += 1
        if B2save != "¤":
            B2save += 1

    if "B2" in bomba:
        if A1save != "¤":
            A1save += 1
        if A2save != "¤":
            A2save += 1
        if A3save != "¤":
            A3save += 1
        if B1save != "¤":
            B1save += 1
        if B3save != "¤":
            B3save += 1
        if C1save != "¤":
            C1save += 1
        if C2save != "¤":
            C2save += 1
        if C3save != "¤":
            C3save += 1

    if "B3" in bomba:
        if A2save != "¤":
            A2save += 1
        if A3save != "¤":
            A3save += 1
        if A4save != "¤":
            A4save += 1
        if B2save != "¤":
            B2save += 1
        if B4save != "¤":
            B4save += 1
        if C2save != "¤":
            C2save += 1
        if C3save != "¤":
            C3save += 1
        if C4save != "¤":
            C4save += 1

    if "B4" in bomba:
        if A3save != "¤":
            A3save += 1
        if A4save != "¤":
            A4save += 1
        if A5save != "¤":
            A5save += 1
        if B3save != "¤":
            B3save += 1
        if B5save != "¤":
            B5save += 1
        if C3save != "¤":
            C3save += 1
        if C4save != "¤":
            C4save += 1
        if C5save != "¤":
            C5save += 1

    if "B5" in bomba:
        if A4save != "¤":
            A4save += 1
        if A5save != "¤":
            A5save += 1
        if B4save != "¤":
            B4save += 1
        if C4save != "¤":
            C4save += 1
        if C5save != "¤":
            C5save += 1

    if "C1" in bomba:
        if B1save != "¤":
            B1save += 1
        if B2save != "¤":
            B2save += 1
        if C2save != "¤":
            C2save += 1
        if D1save != "¤":
            D1save += 1
        if D2save != "¤":
            D2save += 1

    if "C2" in bomba:
        if B1save != "¤":
            B1save += 1
        if B2save != "¤":
            B2save += 1
        if B3save != "¤":
            B3save += 1
        if C1save != "¤":
            C1save += 1
        if C3save != "¤":
            C3save += 1
        if D1save != "¤":
            D1save += 1
        if D2save != "¤":
            D2save += 1
        if D3save != "¤":
            D3save += 1

    if "C3" in bomba:
        if B2save != "¤":
            B2save += 1
        if B3save != "¤":
            B3save += 1
        if B4save != "¤":
            B4save += 1
        if C2save != "¤":
            C2save += 1
        if C4save != "¤":
            C4save += 1
        if D2save != "¤":
            D2save += 1
        if D3save != "¤":
            D3save += 1
        if D4save != "¤":
            D4save += 1

    if "C4" in bomba:
        if B3save != "¤":
            B3save += 1
        if B4save != "¤":
            B4save += 1
        if B5save != "¤":
            B5save += 1
        if C3save != "¤":
            C3save += 1
        if C5save != "¤":
            C5save += 1
        if D3save != "¤":
            D3save += 1
        if D4save != "¤":
            D4save += 1
        if D5save != "¤":
            D5save += 1

    if "C5" in bomba:
        if B4save != "¤":
            B4save += 1
        if B5save != "¤":
            B5save += 1
        if C4save != "¤":
            C4save += 1
        if D4save != "¤":
            D4save += 1
        if D5save != "¤":
            D5save += 1

    if "D1" in bomba:
        if C1save != "¤":
            C1save += 1
        if C2save != "¤":
            C2save += 1
        if D2save != "¤":
            D2save += 1
        if E1save != "¤":
            E1save += 1
        if E2save != "¤":
            E2save += 1

    if "D2" in bomba:
        if C1save != "¤":
            C1save += 1
        if C2save != "¤":
            C2save += 1
        if C3save != "¤":
            C3save += 1
        if D1save != "¤":
            D1save += 1
        if D3save != "¤":
            D3save += 1
        if E1save != "¤":
            E1save += 1
        if E2save != "¤":
            E2save += 1
        if E3save != "¤":
            E3save += 1

    if "D3" in bomba:
        if C2save != "¤":
            C2save += 1
        if C3save != "¤":
            C3save += 1
        if C4save != "¤":
            C4save += 1
        if D2save != "¤":
            D2save += 1
        if D4save != "¤":
            D4save += 1
        if E2save != "¤":
            E2save += 1
        if E3save != "¤":
            E3save += 1
        if E4save != "¤":
            E4save += 1

    if "D4" in bomba:
        if C3save != "¤":
            C3save += 1
        if C4save != "¤":
            C4save += 1
        if C5save != "¤":
            C5save += 1
        if D3save != "¤":
            D3save += 1
        if D5save != "¤":
            D5save += 1
        if E3save != "¤":
            E3save += 1
        if E4save != "¤":
            E4save += 1
        if E5save != "¤":
            E5save += 1

    if "D5" in bomba:
        if C4save != "¤":
            C4save += 1
        if C5save != "¤":
            C5save += 1
        if D4save != "¤":
            D4save += 1
        if E4save != "¤":
            E4save += 1
        if E5save != "¤":
            E5save += 1

    if "E1" in bomba:
        if D1save != "¤":
            D1save += 1
        if D2save != "¤":
            D2save += 1
        if E2save != "¤":
            E2save += 1

    if "E2" in bomba:
        if D1save != "¤":
            D1save += 1
        if D2save != "¤":
            D2save += 1
        if D3save != "¤":
            D3save += 1
        if E1save != "¤":
            E1save += 1
        if E3save != "¤":
            E3save += 1

    if "E3" in bomba:
        if D2save != "¤":
            D2save += 1
        if D3save != "¤":
            D3save += 1
        if D4save != "¤":
            D4save += 1
        if E2save != "¤":
            E2save += 1
        if E4save != "¤":
            E4save += 1

    if "E4" in bomba:
        if D3save != "¤":
            D3save += 1
        if D4save != "¤":
            D4save += 1
        if D5save != "¤":
            D5save += 1
        if E3save != "¤":
            E3save += 1
        if E5save != "¤":
            E5save += 1

    if "E5" in bomba:
        if D4save != "¤":
            D4save += 1
        if D5save != "¤":
            D5save += 1
        if E4save != "¤":
            E4save += 1

def Pole():    
    global i
    for i in range(100):
        print(" ")
    
    print("      ║ 1 ║ 2 ║ 3 ║ 4 ║ 5 ║")
    print("══════╬═══╬═══╬═══╬═══╬═══╣")
    print(f"  A   ║ {A1} ║ {A2} ║ {A3} ║ {A4} ║ {A5} ║")
    print("══════╬═══╬═══╬═══╬═══╬═══╣")
    print(f"  B   ║ {B1} ║ {B2} ║ {B3} ║ {B4} ║ {B5} ║")
    print("══════╬═══╬═══╬═══╬═══╬═══╣")
    print(f"  C   ║ {C1} ║ {C2} ║ {C3} ║ {C4} ║ {C5} ║")
    print("══════╬═══╬═══╬═══╬═══╬═══╣")
    print(f"  D   ║ {D1} ║ {D2} ║ {D3} ║ {D4} ║ {D5} ║")
    print("══════╬═══╬═══╬═══╬═══╬═══╣")
    print(f"  E   ║ {E1} ║ {E2} ║ {E3} ║ {E4} ║ {E5} ║")
    print("══════╩═══╩═══╩═══╩═══╩═══╝")    

dobry = False
vlajecky = [] 

Pripravahry()

while konec == False:
    dobry = False
    Pole()

    kolo = 0
    print(" ")
    print("1) Vybrání políčka")
    print("2) Položit vlaječku")
    print("3) Odebrat vlaječku")
    while dobry == False:
        
        kolo = input("Vyberte si co chete dělat: ")
        try:
            kolo = int(kolo)
            if 0<kolo<4:
                dobry = True
            else:
                print("Zdali jste špatnou hodnotu!!")
        except ValueError:
            print("Zdali jste špatnou hodnotu!!")

    print(" ")    
    dobry = False
    if kolo ==1 :
        while dobry == False:   
            vybranysloupec = input("Vybrte si sloupec (1-5): ")
            try:
                vybranysloupec = int(vybranysloupec)
                if 0<vybranysloupec<6:
                    dobry=True
                    str(vybranysloupec)
                else:
                    print("Zdali jste špatnou hodnotu!!")
            except ValueError:
                print("Zdali jste špatnou hodnotu!!")
        dobry=False
        print(" ")
        while dobry == False:
            vybranyradek = input("Vyberte si řádek(velké písmo!!)(A-E): ")
            try:
                vybranyradek = str(vybranyradek)
                if vybranyradek == "A" or vybranyradek == "B" or vybranyradek == "C" or vybranyradek == "D" or vybranyradek == "E":
                    dobry=True
                else:
                    print("Zdali jste špatnou hodnotu!!")
            except ValueError:
                print("Zdali jste špatnou hodnotu!!")
        dobry = False
        vybrano = vybranyradek + str(vybranysloupec)
        
        Vybranepole(vybrano)

        if Kontorlamin(vybrano) == True:
            break
    elif kolo == 2:
        while dobry == False:   
            vybranysloupec = input("Vybrte si sloupec (1-5): ")
            try:
                vybranysloupec = int(vybranysloupec)
                if 0<vybranysloupec<6:
                    dobry=True
                    str(vybranysloupec)
                else:
                    print("Zdali jste špatnou hodnotu!!")
            except ValueError:
                print("Zdali jste špatnou hodnotu!!")
        dobry=False
        print(" ")
        while dobry == False:
            vybranyradek = input("Vyberte si řádek(velké písmo!!)(A-E): ")
            try:
                vybranyradek = str(vybranyradek)
                if vybranyradek == "A" or vybranyradek == "B" or vybranyradek == "C" or vybranyradek == "D" or vybranyradek == "E":
                    dobry=True
                else:
                    print("Zdali jste špatnou hodnotu!!")
            except ValueError:
                print("Zdali jste špatnou hodnotu!!")
        dobry = False
        vybrano = vybranyradek + str(vybranysloupec)
        
        
        dobry = False
        if len(vlajecky) != 7:    
            vybrano = vybranyradek + str(vybranysloupec)
            Vlajecky(vybrano)
            vlajecky.append(vybrano)
        else:
            print("Maximálně mužete dát 7 vlaječek!!")
            time.sleep(5)
    elif kolo==3:
        while dobry == False:   
            vybranysloupec = input("Vybrte si sloupec (1-5): ")
            try:
                vybranysloupec = int(vybranysloupec)
                if 0<vybranysloupec<6:
                    dobry=True
                    str(vybranysloupec)
                else:
                    print("Zdali jste špatnou hodnotu!!")
            except ValueError:
                print("Zdali jste špatnou hodnotu!!")
        dobry=False
        print(" ")
        while dobry == False:
            vybranyradek = input("Vyberte si řádek(velké písmo!!)(A-E): ")
            try:
                vybranyradek = str(vybranyradek)
                if vybranyradek == "A" or vybranyradek == "B" or vybranyradek == "C" or vybranyradek == "D" or vybranyradek == "E":
                    dobry=True
                else:
                    print("Zdali jste špatnou hodnotu!!")
            except ValueError:
                print("Zdali jste špatnou hodnotu!!")
        dobry = False
        vybrano = vybranyradek + str(vybranysloupec)
        
        
        dobry = False
        vybrano = vybranyradek + str(vybranysloupec)
        if vybrano in vlajecky:
            vlajecky.remove(vybrano)
            VylejckaRemove(vybrano)
        else:
            print(" ")
            print("Zdali jste špatnou hodnotu, na tomto poli vlaječka není!!")
            time.sleep(5)    
    
    if bomba == vlajecky:
        Pole()
        print(" ")
        print("Gratuluji, našli jste všechny miny!!")    
        break
        
        
    

    

        
        
    