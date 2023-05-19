import matika

vypocet = matika.vypocty()
x = int(input('Zadaj prve cislo:\n'))
vypocet.a = x
y = int(input('Zadaj druhe cislo:\n'))
print('Sucet:', vypocet.sucet(y))
print('Rozdiel:', vypocet.rozdiel(y))
print('Sucin:', vypocet.sucin(y))
print('Podiel:', vypocet.podiel(y))
print('Mocnina:', vypocet.mocnina(y))
