from functools import reduce

with open("vastaukset.txt") as f:
    vastaukset = f.read()

ryhmat = vastaukset.split("\n\n")
siistit_ryhmat = [r.replace("\n", "") for r in ryhmat]
kaikkien_summa = reduce(lambda kokonaissumma, ryhma: kokonaissumma + len(set(ryhma)), siistit_ryhmat, 0)

# vastaus 1
print(kaikkien_summa)


ryhmat_yksiloittain = [r.split("\n") for r in ryhmat]

kirjaimia_kaikilla = 0
for r in ryhmat_yksiloittain:
    for k in r[0]:
        for j in r:
            if k not in j:
                break
        else:
            kirjaimia_kaikilla += 1

# vastaus 2
print(kirjaimia_kaikilla)
