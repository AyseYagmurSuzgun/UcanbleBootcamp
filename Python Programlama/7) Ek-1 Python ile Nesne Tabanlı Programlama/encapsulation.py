# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 12:44:46 2025

@author: Asus
"""

class BankAccount:
    
    def __init__(self, name, money, address):
        self.name=name #global
        self.__money=money #private
        self.address=address
        
    # get and set global
    def getMoney(self):
        return self.__money
    
    def setMoney(self, amount):
        self.__money=amount
        
    #private
    def __increase(self):
        self.__money=self.__money+500
        
p1=BankAccount("messi", 1000, "barcelona")
p2=BankAccount("neymar", 2000, "paris")

print("get method: ",p1.getMoney())
#print("get method: ",p1.__money)
p1.setMoney(5000)
print("after set method: ",p1.getMoney())

#p1.__increase()
#print("aftern raise: ",p1.getMoney())