
def sucet(n):
    if n == 0:
        suc = 0
    if n>0:
        suc = n + sucet(n-1)
    return suc

vstup = int(input('Zadaj cislo:\n'))
print(sucet(vstup))
