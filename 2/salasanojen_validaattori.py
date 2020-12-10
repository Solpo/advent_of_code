with open("salasanat.txt") as f:
    salasanat = f.read()

osumia = 0
for rivi in salasanat.split("\n"):
    numerot, kirjain, salasana = rivi.strip().split(" ")
    ala, yla = [int(x) for x in numerot.split("-")]
    kirjain = kirjain[0]
    if salasana.count(kirjain) >= ala and salasana.count(kirjain) <= yla:
        print("mätsäävä salasana!")
        print(f"Salasana oli {salasana}, kirjain {kirjain} ja määrä {ala} - {yla}.")
        osumia += 1

print(osumia)
