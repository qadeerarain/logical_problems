#2. Create a program that asks the user to enter their age and prints out whether they are a child, 
#teenager, adult, or senior citizen.

age=int(input("enter a age"))

if age<=12:
    print("teenager")
else:
    print("adult")