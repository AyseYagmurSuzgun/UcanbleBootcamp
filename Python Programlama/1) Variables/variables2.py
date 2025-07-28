# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 15:52:45 2025

@author: Asus
"""

#%%
# list
liste=[1,2,3,4,5,6]
liste2=[2,5,3,4,6,7]
type(liste)

liste_str=["pazartesi","sali","carsamba"]
type(liste_str)

value=liste[1]
print(value)

last_value=liste[-1]
liste_divide=liste[0:3]

liste.append(7) #listeye 7 degerini ekler
liste.remove(7) #listeden 7 degerini cikarir
liste.reverse() #listeyi ters çevirir
liste2.sort() #listeyi siralar

string_int_liste=["ali","veli",6,4,3]

#%%
# tuple
tuple=(1,2,3,4,4,4,5,6)
tuple.count(4) #tupledaki 4 degerini sayar
tuple.index(4) #tupledaki 4 degerinin indexini verir: 3

#%%
# dictionary
dictionary={"pazartesi":1,"sali":2,"carsamba":3}
#keys: pazartesi,sali,carsamba
#values: 1,2,3

def deneme():
    dictionary={"pazartesi":1,"sali":2,"carsamba":3},
    return dictionary

dic=deneme()

#%%
# conditionals
# if-else statement
var1=10
var2=20

if (var1>var2):
    print("var1,var2'den buyuktur")
elif (var1<var2):
    print("var1,var2'den kucuktur")
else:
    print("var1,var2'ye esittir ")

liste=[1,2,3,4,5]
value=3
if value in liste:
    print("{} degeri listenin icinde vardir".format(value))
else:
    print("{} degeri listede yoktur".format(value))
    
keys=dictionary.keys()
if "persembe" in keys:
    print("evet")
else:
    print("hayir")
    
#%%
# QUIZ-2
# 1640. yil == 17. yuzyil
# 109. yil == 2. yuzyil
# 2000. yil = 20. yuzyil
    
# metod yazin.
    # input integer yillar
    # output integer yuzyil

# input = year  >> 1 <= year <= 2005

def yearCentury(year):
    str_year=str(year)
    if(len(str_year)<3):
        return 1
    elif(len(str_year)==3):
        if(str_year[1:3]=="00"): #100,200,....,900
            return int(str_year[0])
        else: #190,250,450
            return int(str_year[0])+1
    else: #1750,1700,1805
        if(str_year[2:4]=="00"): #1700,1900,1200
            return int(str_year[:2])
        else: #1705,1645,1258
            return int(str_year[:2])+1
        
#%%
# for loop
for each in range(1,11):
    print(each)
    
for each in "balıkesir muğla":
    print(each)
    
for each in "balıkesir muğla".split():
    print(each)
    
liste=[1,2,3,4,5,6,7]
toplam=sum(liste)

count=0
for each in liste:
    count=count+each
    print(count)
    
#%%
# while loop
i=0
while(i<4):
    print(i)
    i=i+1

son=len(liste)
each=0
count=0
while(each<son):
    count=count+liste[each]
    each=each+1 
    
#%%
# QUIZ-3
# liste verecegim
# sizden bu listenin icindeki en kucuk sayiyi bulmanizi istiyorum

liste=[1,3,2,4,6,5,77,65,-9,-34,45,-45]
mini=10000
for each in liste:
    if (each < mini):
        mini=each
    else:
        continue

print(mini)

# hazir fonksiyon kullanarak cozme
liste.sort()
print(liste[0])
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    