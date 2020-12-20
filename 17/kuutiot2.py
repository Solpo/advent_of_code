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

def tyhja_4d_matriisi(pituus: int) -> list:
    matriisi = []
    for _ in range(pituus):
        avaruus = []
        for __ in range(pituus):
            taso = []
            for ___ in range(pituus):
                suora = []
                for ____ in range(pituus):
                    suora.append(".")
                taso.append(suora)
            avaruus.append(taso)
        matriisi.append(avaruus)
    return matriisi

mat = tyhja_4d_matriisi(22)

def lahtodata_matriisiin(lahtodata: list, matriisi: list) -> list:
    
    å = len(matriisi) // 2
    z = len(matriisi[0]) // 2
    y = len(matriisi[0][0]) // 2 - len(lahtodata) // 2
    x = len(matriisi[0][0][0]) // 2 - len(lahtodata[0]) // 2
    

    for rivi in range(len(lahtodata)):
        matriisi[å][z][y + rivi][x:x+len(lahtodata[0])] = lahtodata[rivi]

    return matriisi

mat = lahtodata_matriisiin(lahtodata, mat)

tyomatriisi = copy.deepcopy(mat)

def naapurit(å: int, z: int, y: int, x: int) -> list:
    kaikki = [(å2, z2, y2, x2) for å2, z2, y2, x2 in itertools.product([å-1, å, å+1], [z-1, z, z+1], [y-1, y, y+1], [x-1, x, x+1])]
    kaikki.remove((å, z, y, x))
    siistittava = copy.deepcopy(kaikki)
    for å2, z2, y2, x2 in kaikki:
        if å2 < 0 or z2 < 0 or y2 < 0 or x2 < 0 or å2 >= len(mat) or z2 >= len(mat[å]) or y2 >= len(mat[å][z]) or x2 >= len(mat[å][z][y]):
            siistittava.remove((å2, z2, y2, x2))
    return siistittava

def naapureita_elossa(å: int, z: int, y: int, x: int) -> int:
    elossa = 0
    for nå, nz, ny, nx in naapurit(å, z, y, x):
        if mat[nå][nz][ny][nx] == "#":
            elossa += 1
    return elossa

def paivita_ruutu(å: int, z: int, y: int, x: int):
    ymparilla = naapureita_elossa(å, z, y, x)
    if mat[å][z][y][x] == "#":
        if (ymparilla == 2 or ymparilla == 3):
            tyomatriisi[å][z][y][x] = "#"
        else:
            tyomatriisi[å][z][y][x] = "."
    elif mat[å][z][y][x] == ".":
        if ymparilla == 3:
            tyomatriisi[å][z][y][x] = "#"
        else:
            tyomatriisi[å][z][y][x] = "."
    else:
        raise ValueError("Nyt ollaan oudossa ruudussa kun niitä päivitetään")
    

def laske_elossaolijat() -> int:
    elossa = 0
    for å, z, y, x in (itertools.product(range(0, len(mat)), range(0, len(mat[0])), range(0, len(mat[0][0])), range(0, len(mat[0][0][0])))):
        if mat[å][z][y][x] == "#":
            elossa += 1
            if å == 0 or z == 0 or y == 0 or x == 0 or å == len(mat) - 1 or z == len(mat[å]) - 1 or y == len(mat[å][z]) - 1 or x == len(mat[å][z][y]) - 1:
                print("Laidat kolisee!")
    return elossa

kierroksia = 0
while kierroksia < 10:
    for å in range(len(mat)):
        for z in range(len(mat[å])):
            for y in range(len(mat[å][z])):
                for x in range(len(mat[å][z][y])):
                    paivita_ruutu(å, z, y, x)
            # print(f"taso {y} avaruudesta {z} ajasta {å} käyty läpi")
        print(f"avaruus {z} ajasta {å} kierroksella {kierroksia} käyty läpi")
    print(f"aikaulottuvuus {å} käyty läpi")
    mat = copy.deepcopy(tyomatriisi)
    kierroksia += 1
    print(f"Kierroksia käyty {kierroksia}")
    print(f"Sen jälkeen elossaolijoita on {laske_elossaolijat()}")
    print(f"Kierroksia tosiaan ehdittiin käydä {kierroksia}")
    