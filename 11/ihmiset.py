import itertools

matriisi = []
with open("matriisi.txt") as f:
    for rivi in f:
        matriisi.append(rivi.strip())

def ymparoivat_paikat(y: int, x: int, matriisi: list) -> list:
    if y == 0:
        rivit = [y, y + 1]
    elif y == len(matriisi) - 1:
        rivit = [y - 1, y]
    else:
        rivit = [y - 1, y, y + 1]
    if x == 0:
        sarakkeet = [x, x + 1]
    elif x == len(matriisi[0]) - 1:
        sarakkeet = [x - 1, x]
    else:
        sarakkeet = [x - 1, x, x + 1]
    palautettava = list(itertools.product((rivit[i] for i in range(len(rivit))), (sarakkeet[i] for i in range(len(sarakkeet)))))
    palautettava.remove((y, x))
    return palautettava

def paivita_paikka(y, x, matriisi) -> str:
    ymparilla = varattuja_ymparilla(y, x, matriisi)
    if matriisi[y][x] == "L" and ymparilla == 0:
        return "#"
    elif matriisi[y][x] == "#" and ymparilla >= 4:
        return "L"
    else:
        return matriisi[y][x]

def varattuja_ymparilla(y: int, x: int, matriisi: list) -> int:
    varattuja = 0
    for y, x in ymparoivat_paikat(y, x, matriisi):
        if matriisi[y][x] == "#":
            varattuja += 1
    return varattuja


def tarkastuskierros(matriisi: list) -> list:
    palautettava_matriisi = []
    for y in range(len(matriisi)):
        palautettava_matriisi.append([])
        for x in range(len(matriisi[0])):
            palautettava_matriisi[y].append(paivita_paikka(y, x, matriisi))
    return palautettava_matriisi

def kopioi_matriisi(vanha: list) -> list:
    return [rivi[:] for rivi in vanha]

def laske_varatut(matriisi: list) -> int:
    varattuja = 0
    for rivi in matriisi:
        for paikka in rivi:
            if paikka == "#":
                varattuja += 1
    return varattuja

while True:
    uusi_matriisi = tarkastuskierros(matriisi)
    matriisi = kopioi_matriisi(uusi_matriisi)
    print(laske_varatut(matriisi))
