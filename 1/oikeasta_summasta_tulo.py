with open("numerot.txt") as f:
    numerot = [int(rivi.strip()) for rivi in f]

print(numerot)

for i in range(len(numerot)):
    for j in range(i, len(numerot)):
        if numerot[i] + numerot[j] == 2020:
            print(f"Numerot olivat {numerot[i]} ja {numerot[j]}")
            print(f"Niiden tulo on {numerot[i] * numerot[j]}")


for i in range(len(numerot)):
    for j in range(i, len(numerot)):
        for k in range(j, len(numerot)):
            if numerot[i] + numerot[j] + numerot[k] == 2020:
                print(f"Numerot olivat {numerot[i]} ja {numerot[j]} ja {numerot[k]}")
                print(f"Niiden tulo on {numerot[i] * numerot[j] *numerot[k]}")