def faktorial(x):
    for i in range (x-1, 1 , -1):
        x = x*i
    return x

def reverse(x):
    x = str(x)
    for i in range(len(x)-1, -1, -1):
        #temp = x[i]
        #x[i] = x[len(x)-1]
        #x[len(x)-1] = temp
    #x = int(x)
        print(x[i], end = '')
    #return x

vstup = int(input('Zadaj cislo:\n'))
#print('Faktorial:', faktorial(vstup))

reverse(vstup)