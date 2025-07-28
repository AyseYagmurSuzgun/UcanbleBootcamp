# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 12:33:36 2025

@author: Asus
"""

class Calisan:
    zam_orani=1.8
    counter=0
    
    def __init__(self,isim,soyisim,maas):
        self.isim=isim
        self.soyisim=soyisim
        self.maas=maas
        self.email=isim+soyisim+"@gmail.com"
        
        Calisan.counter=Calisan.counter+1
        
    def giveNameSurname(self):
        return self.isim+" "+self.soyisim
    
    def zamYap(self):
        self.maas=self.maas+self.maas*self.zam_orani
        
isci=Calisan("Ali", "Veli", 50000)
print(isci.maas)
print(isci.giveNameSurname())

# class variable
calisan=Calisan("Ali", "Veli", 10000) 
print("İlk maas:",calisan.maas)
calisan.zamYap()
print("Yeni maas:",calisan.maas)

calisan1=Calisan("Ayse", "Demir", 40000)
calisan2=Calisan("Melek", "Temiz", 45000)
calisan3=Calisan("Salih", "Tunca", 30000)

# class example
liste=[calisan,calisan1,calisan2,calisan3]

maxi_maas= -1
index= -1
for each in liste:
    if(each.maas>maxi_maas):
        maxi_maas=each.maas
        index=each
        
print(maxi_maas)
print(index.giveNameSurname())