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
        print('Titel (uit Medium)  : {}'.format(self.titel))
        print('Prijs (uit Medium)  : {}'.format(self.prijs))
    def __str__(self):
        return '"{}" (\u20ac {})'.format(self.titel, self.prijs) # print titel ( prijs)

class Boek(Medium):
    """Een bibliotheek-boek klasse
    """
    def __init__(self, auteur, paginas, **kwargs):
        super().__init__(**kwargs)   # besteed deze attributen uit naar superclass
        self.auteur =  auteur
        self.paginas = paginas
        
    def pr(self):
        super().pr()
        print('Auteur  (uit Boek)  : {}'.format(self.auteur))
        print('Paginas (uit Boek)  : {}'.format(self.paginas))
    def __str__(self):
        sc = super().__str__()
        return '{}, door {} ({} paginas)'.format(sc, self.auteur, self.paginas)

class Dvd(Medium):
    """Een bibliotheek-dvd klasse
    """
    def __init__(self, regisseur, leeftijd, **kwargs):
        super().__init__(**kwargs)   # besteed deze attributen uit naar superclass
        self.regisseur = regisseur
        self.leeftijd = leeftijd
        
    def pr(self):
        super().pr()
        print('regisseur (uit Dvd) : {}'.format(self.regisseur))
        print('leeftijd (uit Dvd)  : {}'.format(self.leeftijd))
    def __str__(self):
        sc = super().__str__()
        return '{}, regisseur {} ({} min leeftijd)'.format(sc, self.regisseur, self.leeftijd)

class Strip(Boek):
    def __init__(self, tekenaar, **kwargs):
        super().__init__(**kwargs)
        self.tekenaar = tekenaar
    def pr(self):
        super().pr()   # voer .pr() van parent class uit
        print('Tekenaar (uit Strip): {}'.format(self.tekenaar))
        

#        titel             prijs   auteur                    aantal blz
lp=Boek(auteur="Mark Lutz & David Ascher", paginas=595,
        titel="Learning Python", prijs=35.50)

#            titel                  prijs  auteur     blz  tekenaar
strx=Strip(titel="Asterix en Cleopatra", prijs=3.95,
           auteur="Goscinny", paginas=32, tekenaar="Uderzo")

#          titel                   prijs   regisseur         min leeft
film=Dvd(titel="2001, a space odyssey", prijs=17.50, 
         regisseur="Stanley Kubrick", leeftijd=12)

lp.pr()      # toon attributen object lp
strx.pr()    # toon attributen object strx
film.pr()
