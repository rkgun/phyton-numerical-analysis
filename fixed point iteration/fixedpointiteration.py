import math
import sys
from sympy import *

def fixedPointIteration(x0, e, N):
    step = 1
    flag = 1
    condition = True
    while condition:
        x1 = g.subs(x,x0)
		x0 = x1
        step = step + 1
        if step > N:
            flag=0
            break
        
        condition = abs(f.subs(x,x1)) > e

    if flag==1:
        print('\n Approximately one root of the equation : %0.8f' % x1)
    else:
        print('\nNot Convergent.')

try:
	sym=input('Your variable symbol:')
	if sym is None or sym=='':
		x=symbols('x')
	else:
		x=symbols(sym)

	f_func=input('Enter a f(x) function..:')
	g_func=input('Enter a G(x) function..:')
	x0 = float(input('Enter start point: '))
	e = float(input('Enter the absolute relative error percentage..: '))
	N = int(input('Enter maximum step count: '))
	f=sympify(f_func)
	g=sympify(g_func)
	fixedPointIteration(x0,e,N)

except SympifyError:
	print("Please check for typos in the equation")
except ValueError:
	print("Value range cannot be entered empty, so an error occurred")
except Exception as e:
    print("Error!! type={} pls comment me this situtiaon :".format(type(e).__name__))