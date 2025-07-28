# -*- coding: utf-8 -*-
"""
Created on Fri Jul  4 11:26:24 2025

@author: Asus
"""

#%%
# variable (degisken)
# variable
var1=10 #integer=int
var2=10.0 #double (float)
gun= "pazartesi" #string=str

#%%
# string
cumle="Bugün günlerden pazartesi"
variable_type=type(cumle) #degiskenin tipini verir: string=str
print(cumle)

var1="balıkesir"
var2="muğla"
var3=var1+var2
print(var3) #balıkesirmuğla

var4="100"
var5="200"
var6=var4+var5
print(var6) #100200

uzunluk=len(var6) #degiskenin uzunluğun verir: 6
var6[3] #degiskenin 3.elemanını getirir(0 dan baslanir)

#%%
# numbers
# int
integer_deneme=-50
# double=float=ondalikli sayi
float_deneme=-30.7

#%%
# built in functions
float1=10.6
int(float1) #tip donusumu yapılır: 10
round(float1) #degiskeni yuvarlar: 11

#%%
# user defined functions
var1=20
var2=50
output=(((var1+var2)*50)/100.0)*var1/var2
print(output)

#%%
# function parametres=input
def islem(a,b):
    output=(((a+b)*50)/100.0)*a/b
    return output

sonuc=islem(var1,var2)
print(sonuc)

#%%
# default functions: cemberin cevre uzunluğu=2*pi*r
def cember_cevresi_hesapla(r,pi=3.14):
    output=2*pi*r
    return output

ornek1=cember_cevresi_hesapla(2)
print(ornek1)

#%%
# flexible functions
def hesapla(boy,kilo,*args): # *args ifadesi boy ve kilodan sonra gelen tüm parametreler için kullanılır
    print(args)
    output=(boy+kilo)*args[0]
    return output

ornek2=hesapla(170,50,10,20,30)
print(ornek2)

#%%
# QUIZ
# int variable yas
# string isim
# fonksiyonu olacak
# fonksiyon print(type(),len,float())
# *args soyisim
# default parametre ayakkabi numarasi

yas=15
isim="ali"
soyisim="veli"

def function_quiz(yas,isim,*args,ayakkabi_numarasi=39):
    print("İsim:",isim,"Yas:",yas,"Ayak numarasi:",ayakkabi_numarasi)
    print(type(isim))
    print(float(yas))
    
    output=args[0]*yas
    return output

sonuc=function_quiz(yas, isim, soyisim)
print("args[0]-yas: ",sonuc)

#%%
# lambda function
def hesapla(x):
    return x*x

sonuc1=hesapla(3)

sonuc2=lambda x: x*x
print(sonuc2(3)) 