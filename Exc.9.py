def palindrom_test(k):
    pal = True
    if k[0] != k[len(k)-1]:
        pal = False
    for i in range (1, (len(k)//2)):
        if k[i] != k[len(k)-1-i]:
            pal = False
    print(pal)

cislo = input('Zadaj cislo:\n')
palindrom_test(cislo)