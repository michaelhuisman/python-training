

## Opg9

import sys

fname = 'weer.txt' 

try:
    fh = open(fname)
except Exception:
    print('Het ging fout met het openen van {}'.format(fname) )

print('--- 9.a File inleze, commentaar skippen')
for line in fh:
    if line.startswith('#'): continue
    line = line.rstrip()
    print(line)
    
print('--- 9.b Gemiddelde uitrekenen ---------------------------')
fh.seek(0)       # "Spoel  bestand terug"
tot = 0
# een andere manier:
temp = [  int(line.split()[1]) for line in fh if not line.startswith('#')  ]
print(temp)
gemiddelde_temp = sum(temp) / len(temp)
print('    Gemiddelde temp: {}' .format(gemiddelde_temp))

print('--- 9.c Opslaan in dict ---------------------------------')
fh.seek(0)
# nu dmv. dict comprehension
#                key      :        value
#           ______/\_____    ________/\________
#          /             \  /                  \
temp_d = { line.split()[0]: int(line.split()[1])   # formule voor nieuw elem
           for line in fh                          # for loop
           if not line.startswith('#')             # filter
         }
print('    Dict: {}'.format(temp_d))

print('--- 9.d Dict afdrukken ----------------------------------')
print('    Steden onder de gemiddelde temp ({:.2f}):'.format(gemiddelde_temp))
for city, temp in temp_d.items():
    if temp < gemiddelde_temp: print('\t{} ({})'.format(city, temp))
    
print('    Steden boven de gemiddelde temp ({:.2f}):'.format(gemiddelde_temp))
for city, temp in temp_d.items():
    if temp > gemiddelde_temp: print('\t{} ({})'.format(city, temp))
