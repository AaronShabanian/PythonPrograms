#gets a b and c of a quadratic equation and computes to find the answer
import math
a = input("Please input a ")
a = int(a)
b = input("Please input b ")
b = int(b)
c = input("Please input c ")
c = int(c)
answerOne = -b+( math.sqrt((b**2)-4*a*c)/(2*a))
answerTwo = -b-( math.sqrt((b**2)-4*a*c)/(2*a))
print(" The answers to your equation are ",answerOne, " and ",answerTwo)
