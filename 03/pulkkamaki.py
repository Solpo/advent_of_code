karttamatriisi = []

with open("kartta.txt") as f:
    for rivi in f:
        karttamatriisi.append([c for c in rivi.strip()])

leveys = len(karttamatriisi[0])
korkeus = len(karttamatriisi)

max_osumia = 0
for x_lahto in range(1):
    osumia = 0
    x = x_lahto
    y = 0
    while y < korkeus:
        osumia += 1 if karttamatriisi[y][x] == "#" else 0
        x = (x + 3) % leveys
        y += 1
    max_osumia = osumia if osumia > max_osumia else max_osumia
    print(osumia)
print(max_osumia)

def lasku(oikealle: int, alas: int) -> int:
    osumia = 0
    x, y = 0, 0
    while y < korkeus:
        osumia += 1 if karttamatriisi[y][x] == "#" else 0
        x = (x + oikealle) % leveys
        y += alas
    return osumia

print("kakkososio")
laskukuviot = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

osumat_kuvioista = 1
for oikealle, alas in laskukuviot:
    print(f"Lasku kuviolla ({oikealle}, {alas})")
    osumat_kuvioista *= lasku(oikealle, alas)
print(osumat_kuvioista)