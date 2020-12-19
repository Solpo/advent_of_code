vuorot = []
with open("data.txt") as f:
    oikein_pain = [int(s) for s in f.read().strip().split(",")]
    vuorot = oikein_pain[::-1]
print(vuorot)

while len(vuorot) < 2020:
    if vuorot[0] in vuorot[1:]:
        vuorot.insert(0, vuorot[1:].index(vuorot[0]) + 1)
    else:
        vuorot.insert(0, 0)
    if len(vuorot) % 10000 == 0:
        print("30 miljoonaa pitäisi kai saada täyteen eli 3000 kymppitonnia. Kymppitonneja:")
        print(len(vuorot) // 10000)

print(vuorot)
print(vuorot[0])