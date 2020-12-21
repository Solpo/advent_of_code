import re

lasku = "1 + 2 * 3 + 4 * 5 + 6"
    
def laske(lasku: str) -> str:
    eka, operaattori, toka = lasku.split(" ")[0:3]
    loput = " " + " ".join(lasku.split(" ")[3:])
    if eka[0] == "(":
        laske(lasku[1:])
    if toka[0] == "(":
        toka = laske
    eka = int(eka)
    toka = int(toka)
    if operaattori == "+":
        return str(eka + toka) + loput
    elif operaattori == "*":
        return str(eka * toka) + loput

while len(lasku.split(" ")) > 3:
    eka, operaattori, toka = lasku.split(" ")[0:3]
    lasku = laske(lasku)
if len(lasku.split(" ")) == 3:
    eka, operaattori, toka = lasku.split(" ")[0:3]
    print(f"vastaus on {int(laske(lasku))}")
