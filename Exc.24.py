def sucet_seba(a):
    sucet = 0
    for i in range(1,(a+1)):
        sucet = sucet + i
    return sucet

cislo = int(input('Zadaj nejake cislo:\n'))
print(sucet_seba(cislo))