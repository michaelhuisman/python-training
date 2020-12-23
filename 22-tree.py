#!/usr/bin/env python3
import os
import sys
import fnmatch
from os.path import join, getsize

root = sys.argv[1]

for dezedir, subdirs, nondirs in os.walk(root):
    for naam in nondirs:
        if fnmatch.fnmatch(naam, '*.py'): # alleen GIF files
            padnaam = join(dezedir, naam)
            try:
                size = getsize(padnaam)
            except OSError:
                pass
        print('file in', dezedir, 'is', naam,'deze is', size, 'bytes')
    if '.git' in subdirs:
        subdirs.remove('.git') # ga niet naar tmp subdir's