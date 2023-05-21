def digit_number(x):
    #ret = str(x)
    #i = 0
    #while ret[i] == '0' or ret[i] == '1' or ret[i] == '2' or ret[i] == '3' or ret[i] == '4' or ret[i] == '5' or ret[i] == '6' or ret[i] == '7' or ret[i] == '8' or ret[i] == '9':
    #    i = i + 1
    #return i
    i = 1
    num = 0
    while x // i != 0:
        i = i * 10
        num = num + 1
    return num

cislo = int(input('Zadaj cislo:\n'))
print(digit_number(cislo))
