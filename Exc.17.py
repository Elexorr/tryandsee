cislo = int(input('Zadaj cislo:\n'))
a = cislo
cislo = oct(cislo)

print(cislo)

b = (a//8)*10 + a%8

print(b)