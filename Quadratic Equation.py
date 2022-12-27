# Solve the quadratic equation ax**2 + bx + c = 0


import cmath
a = float(input('Enter a value: '))
b = float(input('Enter b value: '))
c = float(input('Enter c value: '))

d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are {0} and {1}'.format(sol1,sol2))
