#6. Create a program that asks the user to enter their exam score and prints out their grade based 
#on the following criteria: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

n=int(input("enter a number:"))
if n>90:
    print("GRADE A")
elif n>80:
    print("GRADE B")
elif n>70:
    print("GRADE C")
elif n>60:
    print("GRADE D")
elif n>50:
    print("GRADE E")
else:
    print("GRADE F")