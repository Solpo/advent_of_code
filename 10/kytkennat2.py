import time, functools

def seuraava_valipysakki(lahtoindeksi: int, lista: list) -> int:
    if lahtoindeksi == len(lista) - 1:
        return lahtoindeksi
    for i in range(lahtoindeksi + 1, len(lista) - 1):
        if lista[i] + 3 == lista[i + 1]:
            return i
    else:
        return len(lista) - 1

def luo_valipysakkilista(lista: list) -> list:
    palautettava = [0]
    while seuraava_valipysakki(palautettava[-1], lista) != palautettava[-1]:
        palautettava.append(seuraava_valipysakki(palautettava[-1], lista))
    return palautettava

def relevantit_indeksivalit(lista: list) -> list:
    palautettava = []
    alku = 0
    while True:
        loppu = seuraava_valipysakki(alku, lista)
        palautettava.append((alku, loppu))
        if loppu >= len(lista) - 2:
            palautettava.append((loppu -1, len(lista) - 1))
            break
        alku = loppu + 1
        while lista[alku] + 3 == lista[alku + 1] and seuraava_valipysakki(alku, lista) == alku + 1:
            alku += 1
    return palautettava

def reitteja_valilla(lahtoindeksi: int, maalin_indeksi: int, lista: list) -> int:
    reitteja = 0
    if lahtoindeksi == maalin_indeksi:
        return 1
    if lista[lahtoindeksi] + 3 <= lista[maalin_indeksi] and lista[lahtoindeksi] + 3 in lista:
        reitteja += reitteja_valilla(lista.index(lista[lahtoindeksi] + 3), maalin_indeksi, lista)
    if lista[lahtoindeksi] + 2 <= lista[maalin_indeksi] and lista[lahtoindeksi] + 2 in lista:
        reitteja += reitteja_valilla(lista.index(lista[lahtoindeksi] + 2), maalin_indeksi, lista)
    if lista[lahtoindeksi] + 1 <= lista[maalin_indeksi] and lista[lahtoindeksi] + 1 in lista:
        reitteja += reitteja_valilla(lista.index(lista[lahtoindeksi] + 1), maalin_indeksi, lista)
    return reitteja


adapterit = []
with open("adapterit.txt") as f:
    for rivi in f:
        adapterit.append(int(rivi.strip()))

# Huom! Lisätään seinävirran "adapteri" 0 listaan!
adapterit.append(0)
adapterit.sort()

valipysakit = luo_valipysakkilista(adapterit)

yhdistelmia = []
for alku, loppu in relevantit_indeksivalit(adapterit):
    yhdistelmia.append(reitteja_valilla(alku, loppu, adapterit))

reitteja_kaikkiaan = functools.reduce(lambda kasvava, alkio: kasvava * alkio, yhdistelmia)
print("vastaus / reittejä kaikkiaan")
print(reitteja_kaikkiaan)