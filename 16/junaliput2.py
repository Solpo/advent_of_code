# Loppusanoikseni haluan sanoa, että olisi varmaan voinut
# jossain kohtaa nähdä funktion määrittelyyn ja käyttöön
# vaadittavan vaivan

import re, functools

with open("data.txt") as f:
    data = f.read()

saannot = data.split("\n\n")[0]
avaimet = {}
for rivi in saannot.split("\n"):
    avain = re.search("^[a-z ]+:", rivi).group().replace(":", "")
    valit_avaimessa = []
    
    range_loyto = re.findall("[0-9]+-[0-9]+", rivi)
    for vali in range_loyto:
        ala = int(vali.split("-")[0])
        yla = int(vali.split("-")[1])
        valit_avaimessa.append(range(ala, yla + 1))
    avaimet[avain] = valit_avaimessa

oma_lippu_rivi = data.split("\n\n")[1].replace("your ticket:\n", "")
oma_lippu = [int(x) for x in oma_lippu_rivi.split(",")]

muut_liput = []
moykky_muut_liput = data.split("\n\n")[2].replace("nearby tickets:\n", "").strip()
for lippu in moykky_muut_liput.split("\n"):
    muut_liput.append([int(x) for x in lippu.split(",")])

sotku_valit = [ehto for ehto in (ehdot for ehdot in avaimet.values())]

kaikki_valit = []
for i in sotku_valit:
    for j in i:
        kaikki_valit.append(j)

roska_liput = []
validit_liput = []
for lippu in muut_liput:
    for luku in lippu:
        for vali in kaikki_valit:
            if luku in vali:
                break
        else:
            roska_liput.append(lippu)
            break
    else:
        validit_liput.append(lippu)

avaimeen_mahdolliset_kohdat = {}
for avain in avaimet:
    avaimeen_mahdolliset_kohdat[avain] = [i for i in range(len(validit_liput[0]))]

for lippu in validit_liput:
    for lipun_kohta in range(len(validit_liput[0])):
        for kentta in avaimet:
            for vali in avaimet[kentta]:
                if lippu[lipun_kohta] in vali:
                    break
            else:
                if lipun_kohta in avaimeen_mahdolliset_kohdat[kentta]:
                    avaimeen_mahdolliset_kohdat[kentta].remove(lipun_kohta)

matsaavat_kohdat = []

while len(matsaavat_kohdat) < 20:
    for loytynyt in matsaavat_kohdat:
        for kentta in avaimeen_mahdolliset_kohdat:
            if loytynyt[1] in avaimeen_mahdolliset_kohdat[kentta]:
                avaimeen_mahdolliset_kohdat[kentta].remove(loytynyt[1])
    for kentta in avaimeen_mahdolliset_kohdat:
        if len(avaimeen_mahdolliset_kohdat[kentta]) == 1:
            matsaavat_kohdat.append((kentta, avaimeen_mahdolliset_kohdat[kentta][0]))


print("Oman lipun tiedot")
selvitetty_oma_lippu = [(kentan_nimi, oma_lippu[kohta]) for kentan_nimi, kohta in matsaavat_kohdat]
print(sorted(selvitetty_oma_lippu, key=lambda kentta: kentta[0]))

print("Itse vastaus:")
# on muuten komea rivi 8) 
print(functools.reduce(lambda tulo, uusi: tulo * uusi, [tiedot[1] for tiedot in list(filter(lambda kentta: "departure" in kentta[0], selvitetty_oma_lippu))], 1))
