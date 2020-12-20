import copy, itertools

def lue_data(tiedosto: str) -> list:
    with open(tiedosto) as f:
        alkutila_mat = []
        for rivi in f:
            suora = []
            for merkki in rivi.strip():
                suora.append(merkki)
            alkutila_mat.append(suora)
    return alkutila_mat

lahtodata = lue_data("data.txt")

def tyhja_3d_matriisi(pituus: int) -> list:
    matriisi = []
    for _ in range(pituus):
        taso = []
        for __ in range(pituus):
            suora = []
            for ___ in range(pituus):
                suora.append(".")
            taso.append(suora)
        matriisi.append(taso)
    return matriisi

mat = tyhja_3d_matriisi(30)

def lahtodata_matriisiin(lahtodata: list, matriisi: list) -> list:
    z = len(matriisi) // 2
    y = len(matriisi[0]) // 2 - len(lahtodata) // 2
    x  = len(matriisi[0][0]) // 2 - len(lahtodata[0]) // 2

    for rivi in range(len(lahtodata)):
        matriisi[z][y + rivi][x:x+len(lahtodata[0])] = lahtodata[rivi]

    return matriisi

mat = lahtodata_matriisiin(lahtodata, mat)
tyomatriisi = copy.deepcopy(mat)

def naapurit(z: int, y: int, x: int) -> list:
    kaikki = [(z2, y2, x2) for z2, y2, x2 in itertools.product([z-1, z, z+1], [y-1, y, y+1], [x-1, x, x+1])]
    kaikki.remove((z, y, x))
    siistittava = copy.deepcopy(kaikki)
    for z2, y2, x2 in kaikki:
        if z2 < 0 or y2 < 0 or z2 < 0 or z2 >= len(mat) or y2 >= len(mat[z]) or x2 >= len(mat[z][y]):
            siistittava.remove((z2, y2, x2))
    return siistittava

def naapureita_elossa(z: int, y: int, x: int) -> int:
    elossa = 0
    for nz, ny, nx in naapurit(z, y, x):
        if mat[nz][ny][nx] == "#":
            elossa += 1
    return elossa

def paivita_ruutu(z: int, y: int, x: int):
    ymparilla = naapureita_elossa(z, y, x)
    if mat[z][y][x] == "#":
        if (ymparilla == 2 or ymparilla == 3):
            tyomatriisi[z][y][x] = "#"
        else:
            tyomatriisi[z][y][x] = "."
    elif mat[z][y][x] == ".":
        if ymparilla == 3:
            tyomatriisi[z][y][x] = "#"
        else:
            tyomatriisi[z][y][x] = "."
    else:
        raise ValueError("Nyt ollaan oudossa ruudussa kun niitä päivitetään")

def laske_elossaolijat() -> int:
    elossa = 0
    for z, y, x in (itertools.product(range(0, len(mat)), range(0, len(mat[0])), range(0, len(mat[0][0])))):
        if mat[z][y][x] == "#":
            elossa += 1
    return elossa

kierroksia = 0
while kierroksia < 10:
    for z in range(len(mat)):
        for y in range(len(mat[z])):
            for x in range(len(mat[z][y])):
                paivita_ruutu(z, y, x)
    mat = copy.deepcopy(tyomatriisi)
    kierroksia += 1
    print(f"Kierroksia käyty {kierroksia}")
    print(f"Sen jälkeen elossaolijoita on {laske_elossaolijat()}")
    

