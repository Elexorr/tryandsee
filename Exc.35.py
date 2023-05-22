cislo = int(input('Zadaj cislo:\n'))

for i in range (-cislo,cislo):
    for j in range (1, (cislo+1)-abs(i)):
        print('*', end = '')
    print('')