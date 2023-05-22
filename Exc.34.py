def mocniny(x):
    for i in range(x):
        print('Tretia mocnina', i+1, 'je', (i+1)**3)

cislo = int(input('Zadaj cislo:\n'))
mocniny(cislo)