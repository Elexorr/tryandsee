def find_primenumbers(x,y):
    primenums = []
    for testovane in range(x,y+1):
        prvocislo = True
        for i in range (testovane//2, 1, -1):
            if testovane % i == 0:
                prvocislo = False
        if prvocislo == True:
            primenums.append(testovane)
            #print(testovane, 'je prvocislo')
        else:
            pass
            #print(testovane, 'nie je prvocislo')
    print('V danom intervale su prvocisla:', primenums)

start = int(input('Zadaj prve cislo:\n'))
end = int(input('Zadaj druhe cislo:\n'))
find_primenumbers(start, end)

