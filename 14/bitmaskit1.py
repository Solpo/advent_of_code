class Bitmaskit:
    def __init__(self, tiedosto: str):
        self.muistipaikat = {}
        self.maski = 36 * "X"
        self.tiedosto = tiedosto

    def int_binaariksi(self, luku: int) -> str:
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

    def lue_maski(self, rivi: str):
        self.maski = rivi.strip().split(" ")[-1]

    def maskaa_binaari(self, binaariluku: str) -> int:
        uusi_binaari = ""
        for i in range(36):
            if self.maski[i] == "1":
                uusi_binaari += "1"
            elif self.maski[i] == "0":
                uusi_binaari += "0"
            elif self.maski[i] == "X":
                uusi_binaari += binaariluku[i]
            else:
                print("Feelua maskauksessa, paska maski käytössä")
        
        palautettava_int = 0
        for i in range(36):
            palautettava_int += (2 ** (35 - i)) * int(uusi_binaari[i])

        return palautettava_int
            
    def tallenna_muistiin(self, rivi: str):
        rivi = rivi.replace("mem[", "").replace("] = ", " ").split(" ")
        muistipaikka, luku = (int(rivi[0]), int(rivi[1]))
        binaari = self.int_binaariksi(luku)
        maskattu_int = self.maskaa_binaari(binaari)
        self.muistipaikat[muistipaikka] = maskattu_int


    def suorita(self):
        with open(self.tiedosto) as f:
            for rivi in f:
                if "mask" in rivi:
                    self.lue_maski(rivi)
                elif "mem" in rivi:
                    self.tallenna_muistiin(rivi)
    
    def vastaus(self) -> int:
        vastaus = sum(self.muistipaikat[muistipaikka] for muistipaikka in self.muistipaikat)
        return vastaus

maski = Bitmaskit("data.txt")
maski.suorita()
print(maski.vastaus())