#!/usr/bin/env python3


# lees bestand
text = open("verhaal.txt", "rt")

reg = 0 
words = 0 
chars = 0 
for line in text:
    reg += 1
    words += len(line.split())
    chars += len(line)
print(reg, words, chars)

text.close()
