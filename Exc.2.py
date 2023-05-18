for i in range (0,10):
    print('Aktualne cislo:', i)
    if i < 1:
        print('Predosle cislo:', i)
        print('Sucet:', i + i)
    elif i >= 1:
        print('Predosle cislo:', i-1)
        print('Sucet:', i + (i-1))
    else:
        pass