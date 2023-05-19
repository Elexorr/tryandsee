with open ('test.txt', 'r') as fp:
    obsah = fp.readlines()
for i in range (len(obsah)):
    if i != 4:
        print(obsah[i], end='')