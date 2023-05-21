def input_parameters(a,b):
    a = int(input('Zadaj a:\n'))
    b = int(input('Zadaj b:\n'))
    def sucet(a,b):
        sucet = a+b
        return sucet
    res = sucet(a,b) + 5
    print(res)

input_parameters(1,1)
