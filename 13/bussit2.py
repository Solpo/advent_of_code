def lue_aikataulu(tiedosto) -> (int, list):
    with open(tiedosto) as f:
        f.readline()
        bussit = f.readline().strip().split(",")
        return bussit

bussit = lue_aikataulu("aikataulu.txt")

# print(f"Bussit: {bussit}")

lahtoajat_vuorovalit = []
for i in range(len(bussit)):
    if bussit[i] != "x":
        lahtoajat_vuorovalit.append((i, int(bussit[i])))
        # print(f"indeksi: {i}, bussi {bussit[i]}")

def matsaako(bussi: int, lahtominuutti: int) -> bool:
    viive, vuorovali = lahtoajat_vuorovalit[bussi]
    if (lahtominuutti + viive) % vuorovali == 0:
        return True
    return False

ajan_nollapiste = 0
isoin_matsannut = -1
kasvatus = 1

while isoin_matsannut < len(lahtoajat_vuorovalit) - 1:
    # print(f"testataan lähtöaikaa {ajan_nollapiste}")
    if not matsaako(isoin_matsannut + 1, ajan_nollapiste):
        ajan_nollapiste += kasvatus
    else:
        isoin_matsannut += 1
        kasvatus *= lahtoajat_vuorovalit[isoin_matsannut][1]

print("oikea vastaus")
print(ajan_nollapiste)
