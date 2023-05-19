meno = input('Zadaj meno osoby:\n')
druhemeno = ''
tretiemeno = ''

i = 0
while meno[i] != ' ':
        #print(meno[i], end = '')
        i = i+1

prvemeno = meno[0:i]

print('Prve meno:', prvemeno)

i = len(prvemeno)+1
while meno[i] != ' ':
        #print(meno[i], end = '')
        i = i+1

druhemeno = meno[len(prvemeno)+1:i]
print('Druhe meno:', druhemeno)

tretiemeno = meno[len(prvemeno) + len(druhemeno) + 2:len(meno)]
print('Tretie meno:', tretiemeno)

#while meno[i] != ' ':
#    prvemeno[i] = meno[i]
#    i = i+1
#print(prvemeno)
