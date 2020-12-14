def reitteja_valilla(lahto: int, maali: int, adapterit: list) -> int:
    reitteja = 1
    
    if maali >= len(adapterit) or lahto >= len(adapterit):
        return 1
    if adapterit[lahto] + 3 <= adapterit[maali] and adapterit[lahto] + 3 in adapterit:
        reitteja += 1 + reitteja_valilla(lahto + 3, maali, adapterit)
    if adapterit[lahto] + 2 <= adapterit[maali] and adapterit[lahto] + 2 in adapterit:
        reitteja += 1 + reitteja_valilla(lahto + 2, maali, adapterit)
    if adapterit[lahto] + 1 <= adapterit[maali] and adapterit[lahto] + 1 in adapterit:
        reitteja +=  1 + reitteja_valilla(lahto + 1, maali, adapterit)
    return reitteja

adapterit = []
with open("adapterit.txt") as f:
    for rivi in f:
        adapterit.append(int(rivi.strip()))

# Huom! Lisätään seinävirran "adapteri" 0 listaan!
adapterit.append(0)
adapterit.sort()

# vastaus 1:
muunnokset=[3]
for i in range(0, len(adapterit)-1):
    muunnokset.append(adapterit[i + 1] - adapterit[i])
print(muunnokset.count(1))
print(muunnokset.count(3))
print(f"Yhden muunnokset * kolmen muunnokset = {muunnokset.count(1) * muunnokset.count(3)}")

#vastaus 2

pakkostopit = []
for i in range(len(adapterit) - 2):
    if adapterit[i + 1] - adapterit[i] == 3:
        pakkostopit.append(i)

print("Pakkostopit")
print(pakkostopit)