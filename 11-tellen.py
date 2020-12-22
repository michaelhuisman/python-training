#!/usr/bin/env python3
f=open("verhaal.txt")
tel = {}
for line in f:
    line = line.rstrip()
    for word in line.split():
        # ontdoe woorden van leestekens
        word = word.strip('()?!.:,;\'')
        if word == '':
            continue
        try:
            tel[word] += 1
        except:
            tel[word] = 1
for k in sorted( tel.keys() ):
    print(k+":", tel[k])