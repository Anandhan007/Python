#Write a program that asks the user to enter their name and their age. 
#Print out a message that greets them and that tells them the year that they will turn 100 years old.

from datetime import date
name = input("Enter your name:")
age = int(input("Enter your age:"))
yearsLeft = 100-age
thisYear=date.today().year
year= yearsLeft+thisYear
print("Hi",name,", you will turn 100 in the year",year,"!")
