#! /usr/bin/env python3

a = str(2 ** 1000)
print(a.count('5'))


uurwaarden = "673,1499,82,119341,13,996308,53,7"
losse = uurwaarden.split(',')
sum = sum ([int(i) for i in losse])

tot = 0
l =  len( str(sum))

for num, getal in enumerate(losse):
    #print("Uur ", str(num+1) + ":", getal)
    #print("Uur %2d: %7s" % (num+1, getal))
    format1="Uur {0:2d}: {1:>" + str(l) + "}"
    print(format1.format(num+1, getal))
    #tot += int(getal)

print("Totaal:", sum)
 
