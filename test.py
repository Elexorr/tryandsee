class trojuholnik:
    def vypocitaj_obvod(self):
        obvod = self.a + self.b + self.c
        return obvod
    def urc_pravouhlost(self):
        if self.c ** 2 == self.a ** 2 + self.b ** 2 or self.a ** 2 == self.b ** 2 + self.c ** 2 or self.b ** 2 == self.a ** 2 + self.c ** 2:
            pravouhlost = 'je pravouhly'
        else:
            pravouhlost = 'nie je pravouhly'
        return pravouhlost


nazov = []
zoznam = []

x = 1
while x != 0:
    x = int(input('Vlozit trojuholnik?\n'))
    if x == 1:
        t = input('Zadaj nazov trojuholnika:\n')
        nazov.append(t)
        t = trojuholnik()
        zoznam.append(t)
        t.a = int(input('Zadaj stranu a:\n'))
        t.b = int(input('Zadaj stranu b:\n'))
        t.c = int(input('Zadaj stranu c:\n'))
    else:
        pass

for i in range (0,len(zoznam)):
    print('Obvod trojuholnika', nazov[i], 'je:', zoznam[i].vypocitaj_obvod(), 'a', zoznam[i].urc_pravouhlost())

