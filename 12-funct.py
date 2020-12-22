#!/usr/bin/env python3



def gem(*list):
    """
    Geeft het gemiddelde van de input
    input moeten intergers zijn
    """
    return (sum(list)) / (len(list))

print(gem(1, 5, 2, 33, 5, 16, 7))


def gem2(*list):
    """
    Geeft het gemiddelde van de input
    input moeten intergers zijn
    """
    return (len(list)) , (sum(list)) / (len(list))

a,b = gem2(1, 5, 2, 33, 5, 16, 7)
print( "aantal:" , a , "gem:", b)
