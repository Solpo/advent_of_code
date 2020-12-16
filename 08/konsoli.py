kaskyt = []

with open("bootcode.txt") as f:
    for rivi in f:
        osat = rivi.strip().split(" ")
        kaskyt.append((osat[0], int(osat[1])))

kasitellyt = []
kumuloitunut = 0
i = 0

while i not in kasitellyt:
    kasitellyt.append(i)
    if kaskyt[i][0] == "jmp":
        i += kaskyt[i][1]
        continue
    elif kaskyt[i][0] == "acc":
        kumuloitunut += kaskyt[i][1]
    elif kaskyt[i][0] == "nop":
        pass
    i += 1

#vastaus
print(kumuloitunut)

