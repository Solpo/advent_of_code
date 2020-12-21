import copy, itertools
import kasvatusfunktiot

def lue_data(tiedosto: str) -> list:
    with open(tiedosto) as f:
        alkutila_mat = []
        for rivi in f:
            suora = []
            for merkki in rivi.strip():
                suora.append(merkki)
            alkutila_mat.append(suora)
    return alkutila_mat

def lahtodata_matriisiin(lahtodata: list, matriisi: list) -> list:
    å = len(matriisi) // 2
    z = len(matriisi[0]) // 2
    y = len(matriisi[0][0]) // 2 - len(lahtodata) // 2
    x = len(matriisi[0][0][0]) // 2 - len(lahtodata[0]) // 2

    for rivi in range(len(lahtodata)):
        matriisi[å][z][y + rivi][x:x+len(lahtodata[0])] = lahtodata[rivi]

    return matriisi

def naapurit(å: int, z: int, y: int, x: int, mat: list) -> list:
    kaikki = [(å2, z2, y2, x2) for å2, z2, y2, x2 in itertools.product([å-1, å, å+1], [z-1, z, z+1], [y-1, y, y+1], [x-1, x, x+1])]
    kaikki.remove((å, z, y, x))
    siistittava = copy.deepcopy(kaikki)
    for å2, z2, y2, x2 in kaikki:
        if å2 < 0 or z2 < 0 or y2 < 0 or x2 < 0 or å2 >= len(mat) or z2 >= len(mat[å]) or y2 >= len(mat[å][z]) or x2 >= len(mat[å][z][y]):
            siistittava.remove((å2, z2, y2, x2))
    return siistittava

def naapureita_elossa(å: int, z: int, y: int, x: int, mat: list) -> int:
    elossa = 0
    for nå, nz, ny, nx in naapurit(å, z, y, x, mat):
        if mat[nå][nz][ny][nx] == "#":
            elossa += 1
    return elossa

def paivita_ruutu(å: int, z: int, y: int, x: int, mat: list):
    reunoilla = 0
    ymparilla = naapureita_elossa(å, z, y, x, mat)
    if mat[å][z][y][x] == "#":
        if (ymparilla == 2 or ymparilla == 3):
            tyomatriisi[å][z][y][x] = "#"
            if not reunoilla:
                if å == 0 or z == 0 or y == 0 or x == 0 or å == len(mat) - 1 or z == len(mat[å]) - 1 or y == len(mat[å][z]) - 1 or x == len(mat[å][z][y]) - 1:
                    reunoilla += 1
        else:
            tyomatriisi[å][z][y][x] = "."
    elif mat[å][z][y][x] == ".":
        if ymparilla == 3:
            tyomatriisi[å][z][y][x] = "#"
            if not reunoilla:
                if å == 0 or z == 0 or y == 0 or x == 0 or å == len(mat) - 1 or z == len(mat[å]) - 1 or y == len(mat[å][z]) - 1 or x == len(mat[å][z][y]) - 1:
                    reunoilla += 1
        else:
            tyomatriisi[å][z][y][x] = "."
    else:
        raise ValueError("Nyt ollaan oudossa ruudussa kun niitä päivitetään")
    return reunoilla

def laske_elossaolijat() -> int:
    elossa = 0
    for å, z, y, x in (itertools.product(range(0, len(mat)), range(0, len(mat[0])), range(0, len(mat[0][0])), range(0, len(mat[0][0][0])))):
        if mat[å][z][y][x] == "#":
            elossa += 1
    return elossa

def kasvata_hyperkuutiota(mat: list) -> list:
    vanha_sivu = len(mat)
    for syvyys in range(vanha_sivu):
        for taso in range(vanha_sivu):
            for rivi in range(vanha_sivu):
                mat[syvyys][taso][rivi].insert(0, ".")
                mat[syvyys][taso][rivi].append(".")
            mat[syvyys][taso].insert(0, kasvatusfunktiot.tyhja_rivi(vanha_sivu + 2))
            mat[syvyys][taso].append(kasvatusfunktiot.tyhja_rivi(vanha_sivu + 2))
        mat[syvyys].insert(0, kasvatusfunktiot.tyhja_taso(vanha_sivu + 2))
        mat[syvyys].append(kasvatusfunktiot.tyhja_taso(vanha_sivu + 2))
    mat.insert(0, kasvatusfunktiot.tyhja_kuutio(vanha_sivu + 2))
    mat.append(kasvatusfunktiot.tyhja_kuutio(vanha_sivu + 2))
    return mat

lahtodata = lue_data("data.txt")
mat = kasvatusfunktiot.tyhja_hyperkuutio(len(lahtodata) + 2)
mat = lahtodata_matriisiin(lahtodata, mat)

kierroksia = 0
while kierroksia < 10:
    tyomatriisi = copy.deepcopy(mat)
    reunoja = 0
    for å in range(len(mat)):
        for z in range(len(mat[å])):
            for y in range(len(mat[å][z])):
                for x in range(len(mat[å][z][y])):
                    reunoja += paivita_ruutu(å, z, y, x, mat)
            # print(f"taso {y} avaruudesta {z} ajasta {å} käyty läpi")
        print(f"avaruus {z} ajasta {å} kierroksella {kierroksia} käyty läpi")
    print(f"aikaulottuvuus {å} käyty läpi")
    mat = copy.deepcopy(tyomatriisi)
    kierroksia += 1
    print(f"Kierroksia käyty {kierroksia}")
    print(f"Sen jälkeen elossaolijoita on {laske_elossaolijat()}")
    if reunoja:
        # print("aktiivisia soluja oli jo matriisin reunalla.\nYritetään jälleen kerran kasvattaa matriisia")
        mat = kasvata_hyperkuutiota(mat)
        # print("kasvatettiin")
