class osoba:
    def vytvor_osobu(self):
        self.a = input('Zadaj prve meno:\n')
        self.b = input('Zadaj druhe meno:\n')
        self.c = input('Zadaj tretie meno:\n')
    def vypis_meno(self):
        print(self.a, self.b, self.c)

clovek = input('Zadaj identifikator:\n')
clovek = osoba()
clovek.vytvor_osobu()
clovek.vypis_meno()
