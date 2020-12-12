with open("saannot.txt") as f:
    saannot = f.read()

oman_sisaltavat = []
uudet = ["shiny gold"]

while True:
    tsekattavat = uudet[:]
    uudet = []
    for rivi in saannot.split("\n"):
        for vari in tsekattavat:
            if vari in rivi.split("contain")[1]:
                ulkovari = rivi.split("contain")[0].replace("bags", "").strip()
                if ulkovari not in oman_sisaltavat:
                        oman_sisaltavat.append(ulkovari)
                        uudet.append(ulkovari)
    if len(uudet) == 0:
        break

print(len(oman_sisaltavat))