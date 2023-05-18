def porovnaj(zoznam):
    if zoznam[0] == zoznam[len(zoznam)-1]:
        print('True')
    else:
        print('False')

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

porovnaj(numbers_x)
porovnaj(numbers_y)