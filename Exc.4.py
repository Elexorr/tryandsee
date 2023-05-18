ret = input('Zadaj nejaky retazec:\n')
n = int(input('Kolko prvych znakov odstranit?\n'))
ret = ret[(n):len(ret)]
print(ret)