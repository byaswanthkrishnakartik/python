import cmath
num=eval(input('Enter a number: '))
num_sqrt = cmath.sqrt(num)
print('The suquare root of {0} is {1:0.3f}+{2:0.3f}j'.format(num_sqrt.real,num_sqrt.imag))