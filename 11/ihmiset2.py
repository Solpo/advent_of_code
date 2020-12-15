import itertools

matriisi = []
with open("matriisi.txt") as f:
    for rivi in f:
        matriisi.append(rivi.strip())

def paivita_paikka(y, x, matriisi) -> str:
    ymparilla = varattuja_ymparilla(y, x, matriisi)
    if matriisi[y][x] == ".":
        return "."
    elif matriisi[y][x] == "L" and ymparilla == 0:
        return "#"
    elif matriisi[y][x] == "#" and ymparilla >= 5:
        return "L"
    else:
        return matriisi[y][x]

def varattuja_ymparilla(y: int, x: int, matriisi: list) -> int:
    varattuja = 0
    suunnat = [ylhaalla, alhaalla, vasemmalla, oikealla, oy, oa, va, vy]
    for suunta in suunnat:
        varattuja += suunta(y, x, matriisi)
    return varattuja



def sisalla(y: int, x: int, matriisi: list) -> bool:
    return True if y >= 0 and y < len(matriisi) and x >= 0 and x < len(matriisi[y]) else False

def ylhaalla(y, x, matriisi) -> int:
    y -= 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        y -= 1
    return 0

def alhaalla(y, x, matriisi) -> int:
    y += 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        y += 1
    return 0

def vasemmalla(y, x, matriisi) -> int:
    x -= 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        x -= 1
    return 0

def oikealla(y, x, matriisi) -> int:
    x += 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        x += 1
    return 0

def oy(y, x, matriisi) -> int:
    y -= 1 
    x += 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        y -= 1 
        x += 1
    return 0

def oa(y, x, matriisi) -> int:
    y += 1 
    x += 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        y += 1 
        x += 1
    return 0

def va(y, x, matriisi) -> int:
    y += 1 
    x -= 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        y += 1 
        x -= 1
    return 0

def vy(y, x, matriisi) -> int:
    y -= 1 
    x -= 1
    while sisalla(y, x, matriisi):
        if matriisi[y][x] == "L":
            return 0
        if matriisi[y][x] == "#":
            return 1
        y -= 1 
        x -= 1
    return 0

def tarkastuskierros(matriisi: list) -> list:
    palautettava_matriisi = []
    for y in range(len(matriisi)):
        palautettava_matriisi.append([])
        for x in range(len(matriisi[0])):
            palautettava_matriisi[y].append(paivita_paikka(y, x, matriisi))
    return palautettava_matriisi

def laske_varatut(matriisi: list) -> int:
    varattuja = 0
    for rivi in matriisi:
        for paikka in rivi:
            if paikka == "#":
                varattuja += 1
    return varattuja

def kopioi_matriisi(vanha: list) -> list:
    return [rivi[:] for rivi in vanha]

while True:
    uusi_matriisi = tarkastuskierros(matriisi)
    matriisi = kopioi_matriisi(uusi_matriisi)
    print(laske_varatut(matriisi))
