def sucet(a,b):
    c = a + b
    d = c + sucet(a,b)
    print(d)

x = int(input('Zadaj a:\n'))
y = int(input('Zadaj b:\n'))
print(sucet(x,y))