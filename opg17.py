#!/usr/bin/env python3

class Medium(object):
    """Een bibliotheek-medium klasse
    bedoeld als superclass van echte media
    """
    def __init__(self, titel, prijs):
        self.titel = titel
        self.prijs = prijs
    def pr(self):
        print('-' * 80)   # om visueel de verschillende objecten van elkaar te
                          # scheiden
        print('Titel (uit Medium): {}'.format(self.titel))
        print('Prijs (uit Medium): {}'.format(self.prijs))

class Boek(Medium):
    """Een bibliotheek-boek klasse
    """
    def __init__(self, titel, prijs, auteur, paginas):
        super().__init__(titel, prijs)   # besteed deze attributen uit naar superclass
        self.auteur =  auteur
        self.paginas = paginas
        
    def pr(self):
        super().pr()
        print('Auteur  (uit Boek): {}'.format(self.auteur))
        print('Paginas (uit Boek): {}'.format(self.paginas))

class Strip(Boek):
    def __init__(self, titel, prijs, auteur, paginas, tekenaar):
        super().__init__(titel, prijs, auteur, paginas)
        self.tekenaar = tekenaar
    def pr(self):
        super().pr()   # voer .pr() van parent class uit
        print('Tekenaar (uit Strip): {}'.format(self.tekenaar))
        

#        titel             prijs   auteur                    aantal blz
lp=Boek("Learning Python", 35.50, "Mark Lutz & David Ascher", 595)

#            titel                  prijs  auteur     blz  tekenaar
strx=Strip("Asterix en Cleopatra", 3.95, "Goscinny", 32, "Uderzo")

#          titel                   prijs   regisseur         min leeft
#film=Dvd("2001, a space odyssey", 17.50, "Stanley Kubrick", 12)

lp.pr()      # toon attributen object lp
strx.pr()    # toon attributen object strx
#film.pr()
