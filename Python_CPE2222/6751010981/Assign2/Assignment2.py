print ("Area of Triangle\n"+"-"*20)
ba = float(input("Enter Base : "))
hi = float(input("Enter Height : "))
print(f"The area is {1/2 * ba * hi:.2f}\n"+"*"*20)

print ("Area of Rectangle\n"+"-"*20)
Le = float(input("Enter Length : "))
Wi = float(input("Enter Width : "))
print(f"The area is {Le*Wi:.2f}\n"+"*"*20)

print ("The Longest size of Right Triangle\n"+"-"*20)
A = float(input("Enter length of the 1st size : "))
B = float(input("Enter length of the 2nd size : "))
import math
print(f"The area is {math.sqrt(A**2 + B**2):.2f}\n"+"*"*20)

print ("The Solution of Quadratic Formula\n"+"-"*20)
c = float(input("Enter Constant('c') : "))
b = float(input("Enter Coefficient of Linear Term('b') : "))
a = float(input("Enter Coefficient of Quadratic Term('a') : "))
import cmath
x1 = (-b + (cmath.sqrt(b**2 - (4*a*c))))/(2*a)
x2 = (-b - (cmath.sqrt(b**2 - (4*a*c))))/(2*a)
print(f"The 1st solution is x = ({x1.real:.18f} + {x1.imag:.18f}j)")
print(f"The 2nd solution is x = ({x2.real:.18f} + {x2.imag:.18f}j)")
print ("*"*20)

print ("Distance of 2 points\n"+"-"*20)
X1 = float(input("Enter x of the 1st point : "))
Y1 = float(input("Enter y of the 1st point : "))
X2 = float(input("Enter x of the 2nd point : "))
Y2 = float(input("Enter y of the 2nd point : "))
print(f"The area is {math.sqrt(((X2-X1)**2)+((Y2-Y1)**2)):.2f}\n"+"*"*20)
