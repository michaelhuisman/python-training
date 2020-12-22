#!/usr/bin/env python3

text = open("weer.txt", "rt")
temperatuur = {} 
som = 0.0

for line in text:
    if line[0] == '#':
        continue
    #print(line, end='')
    koppel = line.split()
    waarde = int(koppel[1])
    som += waarde
    temperatuur[koppel[0]] = waarde

#print(temperatuur)

gemtemp = som / len(temperatuur)
print("Gemiddelde temperatuur:", gemtemp)

koeler = {}
warmer = {}
for stad in temperatuur:
    if temperatuur[stad] < gemtemp:
        koeler[stad] = temperatuur[stad]
    else:
        warmer[stad] = temperatuur[stad]



print("Koelere steden:")
for stad in koeler:
    print("\t", stad, koeler[stad])
print()
print("Warmere steden:")
for stad in warmer:
    print("\t", stad, warmer[stad])