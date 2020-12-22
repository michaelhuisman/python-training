#!/usr/bin/env python3


# lees bestand
text = open("limerick.txt", "rt")

reg = 0 
words = 0 
chars = 0 
bites = 0

for line in text:
    reg += 1
    words += len(line.split())
    chars += len(line)
    bites += len(line.encode('utf-8'))
print(reg, words, chars, bites)

text.close()
