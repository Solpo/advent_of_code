def laske(lasku: str) -> str:
    while ")" in lasku:
        seuraava_kiinni = lasku.index(")")
        edeltava_auki = seuraava_kiinni - lasku[seuraava_kiinni::-1].index("(")
        sulkujen_sisalto = laske(lasku[edeltava_auki + 1:seuraava_kiinni])
        lasku = lasku[:edeltava_auki] + sulkujen_sisalto + lasku[seuraava_kiinni + 1:]

    # tässä kohtaa on aina sulut käsitelty ja päästään purkamaan itse lukujen
    # ja operaattorien jonoa. Ne ovat muuttujassa lasku, jota saa sorkkia

    while "+" in lasku:
        splitattu = lasku.split(" ")
        i_plus = splitattu.index("+")
        eka_laskettava = splitattu[i_plus - 1]
        toka_laskettava = splitattu[i_plus + 1]
        splitattu[i_plus - 1] = "1"
        splitattu[i_plus] = "*"
        splitattu[i_plus + 1] = str(int(eka_laskettava) + int(toka_laskettava))
        lasku = " ".join(splitattu)

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