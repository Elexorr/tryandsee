class kvader:
    "reprezentuje kvadre definovane ich troma rozmermi"
    def __init__(self, a=1, b=1, c=1):
        "Inicializuje rozmery novovytvoreneho kvadra, ak nie su nastavene inak"
        self.default_objem()
    def vypocitaj_objem(self):
        "vypocita objem kvadra"
        objem = self.a * self.b * self.c
        return objem
    def vypocitaj_povrch(self):
        "vypocita povrch kvadra"
        povrch = 2*self.a*self.b + 2*self.b*self.c + 2*self.a*self.c
        return povrch
    def porovnaj_objem(self, kk):
        "vydeli objem kvadra objemom ineho kvadra"
        pomer = (self.a * self.b * self.c) / (kk.a * kk.b * kk.c)
        return pomer
    def default_objem(self):
        "prideluje rozmery novovytvorenemu kvadru"
        self.a = 1
        self.b = 1
        self.c = 1

nazvy = []
kvadre = []
x = 1

while x == 1:
    x = int(input('Zadat kvader?\n'))
    if x == 1:
        nazov = input('Zadaj nazov kvadra.\n')
        nazvy.append(nazov)
        nazov = kvader()
        kvadre.append(nazov)
        print(nazov.a, nazov.b, nazov.c)
        nazov.a = int(input('Zadaj stranu a:\n'))
        nazov.b = int(input('Zadaj stranu b:\n'))
        nazov.c = int(input('Zadaj stranu c:\n'))
    else:
        pass

for i in range (0,len(nazvy)):
    print('Objem kvadra', nazvy[i], 'je', kvadre[i].vypocitaj_objem())
    print('Povrch kvadra', nazvy[i], 'je', kvadre[i].vypocitaj_povrch())

def porovnanie_kvadrov():
    print('\nKtore kvadre chces porovnat?')
    kk1 = input('Zadaj kvader 1:\n')
    i1 = nazvy.index(kk1)
    kk2 = input('Zadaj kvader 2:\n')
    i2 = nazvy.index(kk2)
    print('Objem kvadra', nazvy[i1], 'je', kvadre[i1].porovnaj_objem(kvadre[i2]), 'krat vacsi ako objem kvadra', nazvy[i2], '.')

porovnanie_kvadrov()
porovnanie_kvadrov()
