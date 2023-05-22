def fakt(n):
    if n == 0:
        vysledok = 1 # nerekurzívna vetva, ukončenie rekurzie
    else:
        vysledok = n*fakt(n-1) # rekurzívna vetva, volanie funkcie fakt()
    return vysledok

vstup = int(input('Zadaj cislo:\n'))
print(fakt(vstup))

