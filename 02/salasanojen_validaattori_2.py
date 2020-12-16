with open("salasanat.txt") as f:
    salasanat = f.read()

osumia = 0
for rivi in salasanat.split("\n"):
    numerot, kirjain, salasana = rivi.strip().split(" ")
    ala, yla = [int(x) for x in numerot.split("-")]
    kirjain = kirjain[0]
    osuvia_kirjaimia = 0
    osuvia_kirjaimia += 1 if salasana[ala - 1] == kirjain else 0
    osuvia_kirjaimia += 1 if salasana[yla - 1] == kirjain else 0

    osumia += 1 if osuvia_kirjaimia == 1 else 0

print(osumia)
