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
print(f"Yhden muunnoksia {muunnokset.count(1)}, kolmen muunnoksia {muunnokset.count(3)}.")
print(f"Yhden muunnokset * kolmen muunnokset = {muunnokset.count(1) * muunnokset.count(3)}")
