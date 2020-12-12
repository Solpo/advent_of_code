kaskyt = []

with open("bootcode.txt") as f:
    for rivi in f:
        osat = rivi.strip().split(" ")
        kaskyt.append((osat[0], int(osat[1])))

        
def tyosta(kaskyt_sisaan: list, muutosrivi: int) -> (bool, int):
    kaskyt = kaskyt_sisaan[:]
    kasitellyt = []
    kumuloitunut = 0
    i = 0

    if kaskyt[muutosrivi][0] == "jmp":
        kaskyt[muutosrivi] = ("nop", kaskyt[muutosrivi][1])
    elif kaskyt[muutosrivi][0] == "nop":
        kaskyt[muutosrivi] = ("jmp", kaskyt[muutosrivi][1])
    else:
        return False, -1
    
    while i not in kasitellyt:
        kasitellyt.append(i)
        if i == len(kaskyt):
            return (True, kumuloitunut)
        if kaskyt[i][0] == "jmp":
            i += kaskyt[i][1]
            continue
        elif kaskyt[i][0] == "acc":
            kumuloitunut += kaskyt[i][1]
        elif kaskyt[i][0] == "nop":
            pass
        
        i += 1
    
    return (False, kumuloitunut)

    
for muutosrivi in range(len(kaskyt)):
    vastaus = tyosta(kaskyt, muutosrivi)
    if vastaus[0] == True:
        print(f"muutosrivi oli {muutosrivi}")
        # vastaus
        print(f"Kumuloitunut on {vastaus[1]}")