import os

def lue_aikataulu(tiedosto) -> (int, list):
    with open(tiedosto) as f:
        f.readline()
        bussit = f.readline().strip().split(",")
        return bussit

bussit = lue_aikataulu("aikataulu.txt")

print(f"Bussit: {bussit}")

lahtoajat_vuorovalit = []
for i in range(len(bussit)):
    if bussit[i] != "x":
        lahtoajat_vuorovalit.append((i, int(bussit[i])))
        print(f"indeksi: {i}, bussi {bussit[i]}")

lahtoajat_vuorovalit.sort(key=lambda x: x[1], reverse=True)
print(lahtoajat_vuorovalit)


# ajan_nollapiste = lahtoajat_vuorovalit[0][1] - lahtoajat_vuorovalit[0][0]
ajan_nollapiste = 99999999999885 - 50

def matsaako_bussit_minuutilla(bussi: int, lahtominuutti: int) -> bool:
    viive, vuorovali = lahtoajat_vuorovalit[bussi]
    if (lahtominuutti + viive) % vuorovali == 0:
        if bussi >= len(lahtoajat_vuorovalit) - 1:
            return True
        else:
            return matsaako_bussit_minuutilla(bussi + 1, lahtominuutti)
    else:
        return False
while not matsaako_bussit_minuutilla(0, ajan_nollapiste):
    ajan_nollapiste += lahtoajat_vuorovalit[0][1]

print("oikea vastaus")
print(ajan_nollapiste)
with open("vastaus.txt", "w") as vastaus:
    vastaus.write("Vastaus on ")
    vastaus.write(ajan_nollapiste)

os.system("shutdown /s /t 60")