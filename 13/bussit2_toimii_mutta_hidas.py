def lue_aikataulu(tiedosto) -> (int, list):
    with open(tiedosto) as f:
        f.readline()
        bussit = f.readline().strip().split(",")
        return bussit

bussit = lue_aikataulu("esimerkkilistoja.txt")

print(f"Bussit: {bussit}")

lahtoajat_vuorovalit = []
for i in range(len(bussit)):
    if bussit[i] != "x":
        lahtoajat_vuorovalit.append((i, int(bussit[i])))
        print(f"indeksi: {i}, bussi {bussit[i]}")

# lahtoajat_vuorovalit.sort(key=lambda x: x[1], reverse=True)
print(lahtoajat_vuorovalit)

# nollatason_lahtominuutti = lahtoajat_vuorovalit[0][0]
nollatason_lahtominuutti = 0
kutsuva = 0


def kelpaako_seuraava(kutsuva: int, lahtominuutti: int) -> bool:
    lahtoaikojen_ero = lahtoajat_vuorovalit[kutsuva + 1][0] - lahtoajat_vuorovalit[kutsuva][0]
    # # debuggaus-if
    # if kutsuva == 4:
    #     print(f"Jo neljäs kutsuu, lähtöminuutti = {nollatason_lahtominuutti}.")
    if (lahtominuutti + lahtoaikojen_ero) % lahtoajat_vuorovalit[kutsuva + 1][1] == 0:
        if kutsuva + 1 == len(lahtoajat_vuorovalit) - 1:
            return True
        else:
            return kelpaako_seuraava(kutsuva + 1, lahtominuutti + lahtoaikojen_ero)
    else:
        return False


while not nollatason_lahtominuutti % lahtoajat_vuorovalit[0][1] == 0 or not kelpaako_seuraava(0, nollatason_lahtominuutti):
    nollatason_lahtominuutti += lahtoajat_vuorovalit[0][1]

print(nollatason_lahtominuutti)
print(nollatason_lahtominuutti - lahtoajat_vuorovalit[0][0])