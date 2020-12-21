def tyhja_rivi(pituus: int) -> list:
    return ["."] * pituus

def tyhja_taso(pituus: int) -> list:
    palautettava = []
    for _ in range(pituus):
        palautettava.append(tyhja_rivi(pituus))
    return palautettava

def tyhja_kuutio(sivu: int) -> list:
    palautettava = []
    for _ in range(sivu):
        palautettava.append(tyhja_taso(sivu))
    return palautettava

def tyhja_hyperkuutio(sivu: int) -> list:
    palautettava = []
    for _ in range(sivu):
        palautettava.append(tyhja_kuutio(sivu))
    return palautettava