#5. Implement a program that takes a user's input of three numbers and prints out the maximum 
#and minimum among them.

a=int(input("enter a number1: "))
b=int(input("enter a number2: "))
c=int(input("enter a number3: "))

if a>b:
    print("maximum number")
elif a<b:
    print("minimum number")
else:
    print("zero")