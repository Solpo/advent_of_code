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

def liikuta_suuntimaa(komento: str, maara: int) -> (str, int):
    if komento == "N":
        return ("y", maara)
    elif komento == "E":
        return ("x", maara)
    elif komento == "S":
        return ("y", -maara)
    elif komento == "W":
        return ("x", -maara)
    else:
        raise ValueError("Omituista suuntiman liikuttelua")

def kvadrantti(x: int, y: int) -> int:
    if  x >= 0 and y >= 0:
        return 1
    elif x >= 0 and y < 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x < 0 and y >= 0:
        return 4
    else:
        raise ValueError("Omituinen kvadrantti")

def kaanna_suuntimaa(komento: str, maara: int, x: int, y: int) -> (int, int):
    lahtokvadrantti = kvadrantti(x, y)
    if komento == "L":
        komento == "R"
        maara = (360 - maara) % 360

    kvadrantteja_myotapaivaan = maara // 90 % 4
    if kvadrantteja_myotapaivaan == 1:
        return (y , -x)
    elif kvadrantteja_myotapaivaan == 2:
        return (-x, -y)
    elif kvadrantteja_myotapaivaan == 3:
        return (-y , x)
    else:
        raise ValueError("Omituinen kulma, ei nyt kvadrantit mätsää")


def loppusijainti(liikkeet: list) -> (int, int):
    x, y = 0, 0
    suuntima_x, suuntima_y = 10, 1
    
    for liike in liikkeet:
        komento = liike[0]
        maara = int(liike[1:])

        if komento in ["N", "S", "W", "E"]:
            akseli, liike = liikuta_suuntimaa(komento, maara)
            if akseli == "x":
                suuntima_x += liike
            elif akseli == "y":
                suuntima_y += liike
        elif komento in ["L", "R"]:
            suuntima_x, suuntima_y = kaanna_suuntimaa(komento, maara, suuntima_x, suuntima_y)
        elif komento == "F":
            x += maara * suuntima_x
            y += maara * suuntima_y
    

    print(f"Lopullinen sijainti alkuperäiseen verrattuna (x, y): {x}, {y}")
    print(f"Manhattan-etäisyys alkuperäisestä = {abs(x)} + {abs(y)} = {abs(x) + abs(y)}")

liikkeet = lue_tiedosto("komennot.txt")
loppusijainti(liikkeet)