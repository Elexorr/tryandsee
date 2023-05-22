import os

with open ('test.txt', 'r') as fp:
    obsah = fp.readlines()
with open ('novy.txt', 'w') as fw:
    for i in range (len(obsah)):
        if i != 4:
            print(obsah[i], end='')
            fw.write(obsah[i])
    print('\nDone writing')

file_stats = os.stat('test.txt')
print(file_stats.st_size)