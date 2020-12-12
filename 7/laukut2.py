import re, time
saannot = {}

with open("saannot.txt") as f:
    for saanto in f:
        saanto = " ".join([sana for sana in saanto.split(" ") if not re.search("^bag", sana)])
        saannot_list = saanto.split(" contain ")
        if saannot_list[1] == "no other":
            saannot[saannot_list[0]] = []
        else:
            laukut_sisalla = []
            sisalto_list = saannot_list[1].split(" ")
            for i in range((len(sisalto_list) // 3)):
                laukut_sisalla.append((sisalto_list[1 + i * 3] + " " + sisalto_list[2 + i * 3], int(sisalto_list[0 + i * 3])))
                saannot[saannot_list[0]] = laukut_sisalla

def sisalla(orig_vari: str) -> int:

    if saannot[orig_vari] == []:
        return 0
    else:
        kasseja = 0 
        for saanto in saannot[orig_vari]:
            kasseja += saanto[1] * (1 + sisalla(saanto[0]))
        return kasseja

total = sisalla("shiny gold")
print(total)
