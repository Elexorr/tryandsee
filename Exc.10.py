def vyber_parne(l):
    for i in range(0, len(l)):
        if l[i] % 2 == 0:
            list.append(l[i])

def vyber_neparne(l):
    for i in range(0, len(l)):
        if l[i] % 2 == 1:
            list.append(l[i])

list1 = [10, 20, 25, 30, 35, 50, 55, 60]
list2 = [40, 45, 60, 75, 90, 95, 100, 120]

list = []

#for i in range (0, len(list1)):
#    if list1[i] % 2 == 1:
#        list.append(list1[i])
#for i in range(0, len(list2)):
#    if list2[i] % 2 == 0:
#        list.append(list2[i])

vyber_neparne(list1)
vyber_parne(list2)
list.sort()

print(list)

