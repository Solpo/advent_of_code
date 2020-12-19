import itertools

class Bitmaskit:
    def __init__(self, tiedosto: str):
        self.muistipaikat = {}
        self.maski = 36 * "X"
        self.tiedosto = tiedosto

    def luku_binaariksi(self, luku: int) -> str:
        # Sen voisi tehdä näinkin, mutta tämä oli googlattu, binaari 
        # omien käsien tekosia niin mennään sillä.
        # cinaari = '{0:036b}'.format(luku)
        
        binaari = ""
        for i in range(35, -1, -1):
            if luku // 2 ** i == 1:
                binaari += "1"
                luku -= 2 ** i
            else:
                binaari += "0"
        return binaari

    def binaari_luvuksi(self, binaariluku: str) -> int:
        luku = 0
        for i in range(len(binaariluku)):
            luku += (2 ** (len(binaariluku) - 1 - i)) * int(binaariluku[i])
        return luku

    def lue_maski(self, rivi: str):
        self.maski = rivi.strip().split(" ")[-1]


    # KESKEN, JATKA TEHDEN TÄTÄ
    # ITEROI LÄPI YHDISTELMIEN, TEE SEN TUPLEISTA iter(foo):lla
    # iteraattoreita, ja kaiva sieltä stringiin aina (replacella? next(iteraattori))
    def maskaa_muistipaikka(self, muistipaikka: int) -> list:
        muistipaikka_bin = self.luku_binaariksi(muistipaikka)
        kelluvia = self.maski.count("X")
        yhdistelmat = itertools.product("01", repeat=kelluvia)
        maskatut_muistipaikat = []
        for _ in range(2 ** kelluvia):
            tyobinaari = ""
            tyoyhdistelma = iter(next(yhdistelmat))
            for i in range(len(muistipaikka_bin)):
                if self.maski[i] == "X":
                    tyobinaari += next(tyoyhdistelma)
                elif self.maski[i] == "1":
                    tyobinaari += "1"
                elif self.maski[i] == "0":
                    tyobinaari += muistipaikka_bin[i]
            maskatut_muistipaikat.append(self.binaari_luvuksi(tyobinaari))

        return maskatut_muistipaikat

    def tallenna_muistiin(self, rivi: str):
        rivi = rivi.replace("mem[", "").replace("] = ", " ").split(" ")
        muistipaikka, luku = (int(rivi[0]), int(rivi[1]))
        maskatut_muistipaikat = self.maskaa_muistipaikka(muistipaikka)
        for maskattu_muistipaikka in maskatut_muistipaikat:
            self.muistipaikat[maskattu_muistipaikka] = luku

    def suorita(self):
        with open(self.tiedosto) as f:
            for rivi in f:
                if "mask" in rivi:
                    self.lue_maski(rivi)
                elif "mem" in rivi:
                    self.tallenna_muistiin(rivi)
    
    def vastaus(self) -> int:
        return sum(self.muistipaikat[muistipaikka] for muistipaikka in self.muistipaikat)

maski = Bitmaskit("data.txt")
maski.suorita()
print(maski.vastaus())