# -*- coding: utf-8 -*-
"""
Created on Fri May  6 22:10:04 2022

@author: administrator
"""

#Question No.1 

print("QUESTION No.1:")

string_1=str("Python is a case sensitive language")
#printing length of string_1
print("length of string = ",len(string_1))



#printing string_1 in reverse order
print("String in reverse order : ",string_1[::-1])



#slicing string_1
string_2 = string_1[10:27]
print("slice function result : ",string_2)



#making change in string
string_3=string_1[0:10] + "object oriented" + string_1[26:35]
print("changing case sensitive to object orinted : ",string_3)



#printing index of "a" in string_1
print("index of a : ",string_1.find("a"))



#removing white spaces from string_1
print("after removing white spaces result : ",string_1.replace(" ",""))

print("\n")

# Question No.2
print("QUESTION 2:")
print("Enter your name:-")
v1=input()
print("Enter your SID")
v2=input()
print("Enter your department name")
v3=input()
print("Enter your CGPA")
v4=input()
#printing required details
print("Hey",v1," Here!")
print("My SID is", v2)
print("I am from" ,v3, "department and my CGPA is" ,v4,)

print("\n")

# Question No.3

print("QUESTION 3:")
#initialising a and b
a=56
b=10


#printing a&b
print("The value of a&b = ",a&b)


#printing a|b
print("The value of a|b = ",a|b)


#printing a^b
print("The value of a^b = ",a^b)


#left shift both a and b by 2 bits
print("The value of a<<2 = ",a<<2,"\nThe value of b<<2 = ",b<<2)


#right shift a by 2  its and left shift b by 4 bits
print("The value of a>>2 = ",a>>2,"\nThe value of b>>4 = ",b>>4)

print("\n")

#Question No.4

print("QUESTION 4:")
#to check if the word “name” is present in the string entered by the user
print("Enter a sentence")
sentence=str(input())
if(sentence.find("name") >= 0):
     print("true")
else:
    print("false")

print("\n")

# QUESTION NO.5
print("QUESTION 5:")
print("This program tell's that, the sides Entered by the user will form a triangle or not")
#taking length of 3 sides as input from user
print("Enter first side of triangle")
side1=float(input())
print("Enter second side of triangle")
side2=float(input())
print("Enter third side of triangle")
side3=float(input())
A=side1<side2+side3
B=side2<side1+side3
C=side3<side2+side1

Result=str(A&B&C)
print("The sides entered by the user can form a triangle?")
Result=Result.replace("True","YES")
Result=Result.replace("False","NO")
print("The Answer is ",Result)
print("\n")

# QUESTION NO.6
print("QUESTION 6:")
#counting number of bits needed to be flipped to convert ‘a’ to ‘b’
a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
n = a^b
count = 0
while(n>0):
        count += 1
        n &= (n-1)
print("number of bits flipped = ",count)


