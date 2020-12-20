import re

with open("lyhyt.txt") as f:
    data = f.read()

saannot = data.split("\n\n")[0]
avaimet = {}
for rivi in saannot.split("\n"):
    avain = re.search("^[a-z]+", rivi).group()
    avaimen_valit = []
    
    range_loyto = re.findall("[0-9]+-[0-9]+", rivi)
    for vali in range_loyto:
        ala = int(vali.split("-")[0])
        yla = int(vali.split("-")[1])
        avaimen_valit.append(range(ala, yla + 1))
    avaimet[avain] = avaimen_valit

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

print(kaikki_valit)

kelvottomat_luvut = []
kelvolliset_liput = []
for lippu in muut_liput:
    for luku in lippu:
        for vali in kaikki_valit:
            if luku in vali:
                break
        else:
            kelvottomat_luvut.append(luku)
 
print(kelvottomat_luvut)
print(f"Vastaus on {sum(kelvottomat_luvut)}")

