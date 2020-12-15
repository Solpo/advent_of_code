def lue_tiedosto(tiedosto: str):
    liikkeet = []
    with open(tiedosto) as f:
        for r in f:
            liikkeet.append(r.strip())
    return liikkeet


def liikuta(komento: str, maara: int) -> (str, int):
    if komento == "N":
        return ("y", maara)
    if komento == "S":
        return ("y", -maara)
    if komento == "E":
        return ("x", maara)
    if komento == "W":
        return ("x", -maara)
    raise ValueError("Ei validi komento!")

def liikuta_suuntaan(suunta: int, maara: int) -> (str, int):
    if suunta % 360 == 0:
        return ("x", maara)
    elif suunta % 360 == 90:
        return ("y", -maara)
    elif suunta % 360 == 180:
        return ("x", -maara)
    elif suunta % 360 == 270:
        return ("y", maara)
    raise ValueError("Suunta mitä sattuu")


def loppusijainti(liikkeet: list) -> (int, int):
    suunta, x, y = 0, 0, 0
    for liike in liikkeet:
        komento = liike[0]
        maara = int(liike[1:])

        if komento == "R":
            suunta += int(liike[1:])
        elif komento == "L":
            suunta -= int(liike[1:])
        else:
            if komento == "F":
                akseli, muutos = liikuta_suuntaan(suunta, maara)
            elif komento in ["N", "S", "W", "E"]:
                akseli, muutos = liikuta(komento, maara)
            else:
                raise ValueError("Komento omituinen")
            if akseli == "x":
                x += muutos
            elif akseli == "y":
                y += muutos
    print(f"Lopullinen sijainti alkuperäiseen verrattuna (x, y): {x}, {y}")
    print(f"Manhattan-etäisyys alkuperäisestä = {abs(x)} + {abs(y)} = {abs(x) + abs(y)}")

liikkeet = lue_tiedosto("komennot.txt")
loppusijainti(liikkeet)