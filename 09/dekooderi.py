import itertools, time

luvut = []
with open("data.txt") as f:
    for rivi in f:
        luvut.append(int(rivi.strip()))

# ekan vastaus
for i in range(25, len(luvut) -1):
    for x, y in itertools.combinations(luvut[i - 25: i], 2):
        if x + y == luvut[i]:
            # print(f"Pari löytyi, {x} + {y} = {luvut[i]}, i == {i}")
            break
    else:
        ongelma = luvut[i]
        print(f"Ei löytynyt edellisistä, ongelmallinen luku oli {luvut[i]}, (datan {i}:s luku)")
        break


# tokan vastaus
for lahto in range(1000):
    for loppu in range(lahto + 1, 1000):
        if sum(luvut[lahto:loppu]) > ongelma:
            break
        if sum(luvut[lahto:loppu + 1]) == ongelma:
            print(f"Ongelmaluvun tuottaman haarukan eka luku on listan {lahto}:s luku {luvut[lahto]}")
            print(f"Ongelmaluvun tuottaman haarukan vika luku on listan {loppu}:s luku {luvut[loppu]}")
            print(f"Niiden välistä pienin luku on {min(luvut[lahto:loppu+1])}, suurin {max(luvut[lahto:loppu+1])}")
            print(f"Niiden summa on {min(luvut[lahto:loppu+1]) + max(luvut[lahto:loppu+1])}")