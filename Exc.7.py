ret = input('Zadaj hlavny retazec:\n')
test = input('Zadaj hladany retazec\n')

count = 0

for i in range (0, len(ret)-(len(test)-1)):
    if ret[i:i+len(test)] == test:
        count = count + 1

print(count)