liput = []

def id(rivi: int, paikka: int) -> int:
    return rivi * 8 + paikka

with open("lentoliput.txt") as f:
    for lippu in f:
        lippu = lippu.strip()
        rivi = 0
        rivi_bin = lippu[0:7].replace("F", "0").replace("B", "1")
        for i in range(7):
            rivi += int(rivi_bin[i]) * 2 ** (6 - i)
        rivi_2 = int(rivi_bin, 2)
        paikka = 0
        paikka_bin = lippu[7:].replace("R", "1").replace("L", "0")
        for i in range(3):
            paikka += int(paikka_bin[i]) * 2 ** (2 - i)
        paikka_2 = int(paikka_bin, 2)
        liput.append((rivi, paikka))


idt = [x * 8 + y for x, y in liput]
print(f"Suurin id on {max(idt)}")

kaikki_paikat = [(r, p) for r in range(128) for p in range(8)]
for r, p in liput:
    kaikki_paikat.remove((r, p))
print(sorted(kaikki_paikat))

for i in range(89, 889):
    if i not in idt and i - 1 in idt and i + 1 in idt:
        print(f"Oman paikan id: {i}")
        print(f"Paikka on rivi {i // 8} ja istuin {i % 8}")
