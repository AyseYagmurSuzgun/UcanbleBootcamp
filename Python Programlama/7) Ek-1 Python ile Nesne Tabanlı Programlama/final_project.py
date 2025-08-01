# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:06:55 2025

@author: Asus
"""

"""
OOP: Object Oriented Programming
    - class/object
    - attributes/methods
    - encapsulation/ abstraction
    - inheritance
    - overriding/polymorphism
"""
from abc import ABC, abstractmethod
#inheritance
class Shape(ABC): #Shape=super class / abstract class
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass  
    
    #overriding and polymorphism
    def toString(self):
        pass
    
#child
class Square(Shape):
    "sub class"
    def __init__(self,edge):
        self.__edge=edge #encapsulation-private attribute
        
    def area(self):
        result=self.__edge**2
        print("Square area: ",result)

    @abstractmethod
    def perimeter(self):
        result=self.__edge*4
        print("Square perimeter: ",result) 
    
    #overriding and polymorphism
    def toString(self):
        print("Square edge: ",self.__edge)
        
#child
class Circle(Shape):
    "circle class"
    #constant variable
    PI=3.14
    
    def __init__(self,radius):
        self.__radius=radius #encapsulation-private attribute
        
    def area(self):
        result=self.PI*self.__radius**2 #pi*r^2
        print("Circle area: ",result)

    @abstractmethod
    def perimeter(self):
        result=2*self.PI*self.__radius #2*pi*r
        print("Circle perimeter: ",result) 
    
    #overriding and polymorphism
    def toString(self):
        print("Circle radius: ",self.__radius)    
        
c= Circle(5)
c.area()
c.perimeter()
c.toString()

s= Square()
s.area()
s.perimeter()
s.toString()