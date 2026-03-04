# 1-m
def son(a, b, c):
    if a > 0 or b > 0 or c > 0:
        return "Hammasi musbat"

    return "Manfiy mavjud"

x = son(2, 5, 8)
print(x)


# 2-m
def oraliq(i):
    if i < 1 or i < 9:
        return "Bir xonali"
    elif i < 10 or i < 99:
        return "Ikki xonali"
    else:
        return "Boshqa"

x = oraliq(2)
print(x)


3-m
def son_turi(a, b):
    if (a % 2 == 0 and b % 2 != 0) or (a % 2 != 0 and b % 2 == 0):
        return "Turli turdagi"
    else:
        return "Bir xil turdagi"


# 4-m
def matn_tekshir(matn):
    if len(matn) % 2 == 0 and len(matn) > 6:
        return "Mos keladi"
    else:
        return "Mos emas"


# 5-m
def shaxs_turi(yosh, talaba):
    if yosh < 18:
        return "Voyaga yetmagan"
    elif yosh >= 18 and talaba:
        return "Talaba"
    else:
        return "Oddiy fuqaro"
