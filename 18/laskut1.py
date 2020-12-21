import re


# lasku = "(4 * (3 * 2 + 2) * (9 * 7 * 5 * 4 * 9) * (7 * 7 + 7 * 4 + 9)) + 6 * 4 + 8 + ((6 * 5) * 4 * (2 * 8 + 4 + 7 * 9 + 3) * 2 + 6) + 3"
# lasku = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"
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
    while ")" in lasku:
        seuraava_kiinni = lasku.index(")")
        edeltava_auki = seuraava_kiinni - lasku[seuraava_kiinni::-1].index("(")
        sulkujen_sisalto = laske(lasku[edeltava_auki + 1:seuraava_kiinni])
        lasku = lasku[:edeltava_auki] + sulkujen_sisalto + lasku[seuraava_kiinni + 1:]
        # while seuraavat_sulut(lasku[seuraava_auki + 1:]) == "(":
        #     # viimeinen_kiinni = len(lasku) - 1 - lasku[::-1].index(")")
        #     seuraavakin_auki = lasku.index("(")
        #     sulkujen_sisalto = laske(lasku[seuraava_auki + 1:viimeinen_kiinni])
        #     lasku = lasku[:seuraava_auki] + sulkujen_sisalto + lasku[viimeinen_kiinni + 1:]
        # while seuraavat_sulut(lasku[seuraava_auki + 1:]) == ")":
        #     ensimmainen_kiinni = lasku.index(")")
        #     sulkujen_sisalto = laske(lasku[seuraava_auki + 1:ensimmainen_kiinni])
        #     lasku = lasku[:seuraava_auki] + sulkujen_sisalto + lasku[ensimmainen_kiinni + 1:]

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

with open("data.txt") as f:
    laskut = f.read()

vastaukset = []
for rivi in laskut.split("\n"):
    vastaukset.append(int(laske(rivi)))
print(sum(vastaukset))


# tulos = int(laske(lasku))
# print(f"tulos: {tulos}")