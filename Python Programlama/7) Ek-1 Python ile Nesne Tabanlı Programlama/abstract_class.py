# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 14:23:44 2025

@author: Asus
"""

from abc import ABC, abstractmethod

class  Animal(ABC): #superclass
    @abstractmethod
    def walk(self):
        pass
    
    def run(self):
        pass
    
class Bird(Animal): #subclass
    def __init__(self):
        print("bird")
        
    def walk(self):
        print("walk")
        
b1=Bird()