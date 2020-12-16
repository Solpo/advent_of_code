import re

def tarkista(sanakirja: dict) -> bool:
    for kohta in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if not kohta in sanakirja:
            return False
    if len(sanakirja["byr"]) != 4 or int(sanakirja["byr"]) < 1920 or int(sanakirja["byr"]) > 2002:
        return False
    if len(sanakirja["iyr"]) != 4 or int(sanakirja["iyr"]) < 2010 or int(sanakirja["iyr"]) > 2020:
        return False
    if len(sanakirja["eyr"]) != 4 or int(sanakirja["eyr"]) < 2020 or int(sanakirja["eyr"]) > 2030:
        return False
    if "in" not in sanakirja["hgt"] and "cm" not in sanakirja["hgt"]:
        return False
    if "cm" in sanakirja["hgt"]:
        if int(sanakirja["hgt"][:-2]) < 150 or int(sanakirja["hgt"][:-2]) > 193:
            return False
    elif "in" in sanakirja["hgt"]:
        if int(sanakirja["hgt"][:-2]) < 59 or int(sanakirja["hgt"][:-2]) > 76:
            return False
    if not re.search("^#[0-9a-f]{6}$", sanakirja["hcl"]):
        return False
    if not re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", sanakirja["ecl"]):
        return False
    if not re.search("^[0-9]{9}$", sanakirja["pid"]):
        return False
    return True
        

with open("passit.txt") as f:
    passit_str = f.read()

passit_str = passit_str.replace("\n\n", ";")
passit_str = passit_str.replace("\n", " ")
passit_str = passit_str.replace(";", "\n").strip()
sanakirjat = []
vaaria = 0
oikeita = 0
for rivi in passit_str.split("\n"):
    sanakirja = {}
    for yksikko in rivi.split(" "):
        sanakirja[yksikko.split(":")[0]] = yksikko.split(":")[1]
    sanakirjat.append(sanakirja)

for sanakirja in sanakirjat:
    if not tarkista(sanakirja):
        vaaria += 1
    else:
        oikeita += 1

print(f"vääriä: {vaaria}")
print(f"oikeita: {oikeita}")
# for sanakirja in sanakirjat:
#     if "pid" in sanakirja:
#         print(sanakirja["pid"])
    
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
