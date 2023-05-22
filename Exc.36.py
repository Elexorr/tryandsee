def reverse(x):
    i = 10
    cislo = 0
    while x // i != 0:
        cislo = cislo + (x % i)
        i = i * 10 + 2
    return cislo

vstup = int(input('Zadaj cislo:\n'))
print(reverse(vstup))