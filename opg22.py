#!/usr/bin/env python3

import sys
from os import walk
from os.path import getsize, join, exists


if len(sys.argv) != 2:
    print('Ik heb 1 argument nodig!')
    sys.exit(10)
    
root = sys.argv[1]             # arg1: directory

tot = 0                        # teller
for curdir, subdirs, nondirs in walk(root):
    for f in nondirs:          # loop bestanden, symlinks ed. door
        p = join(curdir, f)    # p = padnaam
        try:
            # dit ivm. bv. broken symlinks, permissie errors e.d.
            tot += getsize(p)  # tel filesize op bij totaal
        except Exception as e:
            print('Can bestand {} niet verwerken: {}'.format(p, e.args),
                   file=sys.stderr)
            
print('\n\nTotaal gebruikte diskruimte in dir {}: {} bytes'.format(root, tot))
            
