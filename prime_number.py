# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 12:32:31 2020

@author: aydogdu
"""


num = int(input("Enter a number: "))
Isprime = True



if num>1 :
    for i in range(2,num):
        if num % i ==0:
            Isprime = False
            break                        
    if Isprime==True:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number") 
elif num==1:
    print( "1 is not a prime number") 
else:
      print("Please enter a positive integer number")
