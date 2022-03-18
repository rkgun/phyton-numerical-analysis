import math
import sys
from sympy import *

def secant(x0,x1,e,N):
    step = 1
    condition = True
    while condition:
        if f.subs(x,x0) == f.subs(x,x1):
            print('Divide by zero error!')
            break
        
        x2 = x0 - (x1-x0)*f.subs(x,x0)/( f.subs(x,x1) - f.subs(x,x0) ) 
        x0 = x1
        x1 = x2
        step = step + 1
        
        if step > N:
            print('Not Convergent!')
            break
        
        condition = abs(f.subs(x,x2)) > e
    print('\n Approximately one root of the equation: %0.8f' % x2)



sym=input('Your variable symbol:')
if sym is None or sym=='':
	x=symbols('x')
else:
	x=symbols(sym)

x0,x1 = input('Enter First Guess: ').split()
f_func=input('Enter a f(x) function..:')
e = float(input('Tolerable Error: '))
N = int(input('Maximum Step: '))

x0 = float(x0)
x1 = float(x1)
f=sympify(f_func)

secant(x0,x1,e,N)