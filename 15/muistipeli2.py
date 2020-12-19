sanotut_numerot = {}

with open("data.txt") as f:
    alkuvuorot = [int(s) for s in f.read().strip().split(",")]


for vuoro in range(1, len(alkuvuorot) + 1):
    if vuoro > 1:
        sanotut_numerot[myohemmin_lisattava[0]] = myohemmin_lisattava[1]
    myohemmin_lisattava = (alkuvuorot[vuoro - 1], vuoro)
    viimeksi_sanottu = alkuvuorot[vuoro - 1]

viimeinen_kierros = 30000000

for vuoro in range(len(alkuvuorot) + 1, viimeinen_kierros + 1):
    numero, vuorolla = myohemmin_lisattava
    if viimeksi_sanottu in sanotut_numerot:
        viimeksi_sanottu = vuoro - 1 - sanotut_numerot[viimeksi_sanottu]
    else:
        viimeksi_sanottu = 0
    myohemmin_lisattava = (viimeksi_sanottu, vuoro)

    sanotut_numerot[numero] = vuorolla

print(viimeksi_sanottu)