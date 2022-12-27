a=float(input('Enter First side: '))
b=float(input('Enter Second side:'))
c=float(input('Enter Third side: '))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the traingle is %.2f",area)