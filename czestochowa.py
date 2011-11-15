#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (C) 2011 Maciej Ostaszewski
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.




WYRAZY=4
WIERSZE=10




import random
import re
import sys
from collections import Counter, defaultdict
import string




def czyszczenie(tekst):
    tekst=tekst.strip()
    tekst=re.sub("[^a-zA-ZążśźćęłńóĄŻŚŹĆĘÓŁŃ ]"," ",tekst)
    tekst=re.sub(" +"," ",tekst.lower())
    tekst=tekst.translate(string.maketrans("ĄŻŚŹĘĆŃÓŁ","ążśźęćńół"))
    return tekst

def niepusty(linia):
    if re.search("^ *$",linia):
        wyn=False
    else:
        wyn=True
    return wyn

def zerowy(element):
    if len(element)==0:
        wyn=False
    else:
        wyn=True
    return wyn

def ostatnia(litera,para):
    return litera+":" in para

wyrazy=[]
pary=[]
for pliki in sys.argv[1:len(sys.argv)]:
    plik=open(pliki)
    plik=map(lambda x:czyszczenie(x),plik)
    plik=filter(niepusty,plik)

    ost=len(plik)
    
    try:
        for x in range(1,30):
            if plik.pop()=='-----':
                break
    except IndexError:
        plik=open(pliki)
        plik=map(lambda x:czyszczenie(x),plik)
        plik=filter(niepusty,plik)
        ost=len(plik)


    for linia in plik:
        for wyraz in linia.split(" "):
            wyrazy.append(wyraz.strip())

wyrazy=filter(zerowy,wyrazy)

for (pierwszy,drugi) in zip(wyrazy[0:len(wyrazy)-2],wyrazy[1:len(wyrazy)-1]):
    para=pierwszy+":"+drugi
    try:
        para=para.decode('utf-8')
        pary.append(para)
    except UnicodeDecodeError:
        pass

for x in range(0,WIERSZE):
    wiersz=[]
    para=random.choice(pary).split(":")
    wiersz.append(" ".join(para))
    for y in range(0,WYRAZY/2):
        para=random.choice(filter(lambda x: ostatnia(para[1][-1],x),pary)).split(":")
        wiersz.append(" ".join(para))
    print " ".join((wiersz))

