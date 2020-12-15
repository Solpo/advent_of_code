def lue_aikataulu(tiedosto) -> (int, list):
    with open(tiedosto) as f:
        lahtoaika = int(f.readline().strip())
        bussit = [int(vali) for vali in filter(lambda luku: luku != "x", f.readline().strip().split(","))]
        return lahtoaika, bussit

lahtoaika, bussit = lue_aikataulu("aikataulu.txt")

print(f"Lähtöaika: {lahtoaika}")
print(f"Bussit: {bussit}")


kyyti = False
kyytiinnousu = lahtoaika
while not kyyti:
    for bussi in bussit:
        if kyytiinnousu % bussi == 0:
            print(f"Odotus oli {kyytiinnousu - lahtoaika} minuuttia, matkaan päästiin bussilla {bussi}")
            print(f"Odotus * bussin numero = {kyytiinnousu - lahtoaika} * {bussi} = {(kyytiinnousu - lahtoaika) * bussi}")
            kyyti = True
            break
    kyytiinnousu += 1