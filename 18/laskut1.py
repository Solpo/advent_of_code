import re

lasku = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
# lasku = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
# lasku = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
# lasku = "2 * 3 + (4 * 5)"
# lasku = "1 + 2 * 3 + 4 * 5 + 6"
# lasku = "1 + (2 * 3) + (4 * (5 + 6))"

def seuraavat_sulut(lasku: str) -> str:
    if "(" not in lasku:
        return ")"
    else:
        if lasku.index("(") < lasku.index(")"):
            return "("
        else:
            return ")"

def laske(lasku: str) -> str:
    while "(" in lasku:
        sulun_indeksi = lasku.index("(")
        if seuraavat_sulut(lasku[sulun_indeksi + 1:]) == "(":
            viimeinen_kiinni = len(lasku) - 1 - lasku[::-1].index(")")
            sulkujen_sisalto = laske(lasku[sulun_indeksi + 1:viimeinen_kiinni])
            lasku = lasku[:sulun_indeksi] + sulkujen_sisalto + lasku[viimeinen_kiinni + 1:]
        else:
            ensimmainen_kiinni = lasku.index(")")
            sulkujen_sisalto = laske(lasku[sulun_indeksi + 1:ensimmainen_kiinni])
            lasku = lasku[:sulun_indeksi] + sulkujen_sisalto + lasku[ensimmainen_kiinni + 1:]

    while len(lasku.split(" ")) > 3:
        eka, operaattori, toka = lasku.split(" ")[0:3]
        loput = " ".join(lasku.split(" ")[3:])
            
        eka = int(eka)
        toka = int(toka)
        if operaattori == "+":
            print(f"lasketaan {eka} + {toka} = {eka + toka}")
            lasku = str(eka + toka) + " " + loput
        elif operaattori == "*":
            print(f"lasketaan {eka} * {toka} = {eka * toka}")
            lasku = str(eka * toka) + " " + loput
    
    eka, operaattori, toka = lasku.split(" ")[0:3]
    eka = int(eka)
    toka = int(toka)
    if operaattori == "+":
        print(f"lasketaan {eka} + {toka} = {eka + toka}")
        return str(eka + toka)
    elif operaattori == "*":
        print(f"lasketaan {eka} * {toka} = {eka * toka}")
        return str(eka * toka)

with 

tulos = int(laske(lasku))
print(f"tulos: {tulos}")