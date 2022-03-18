import math
import sys
from sympy import *
try:
	sym=input('Your variable symbol:')
	if sym is None or sym=='':
		x=symbols('x')
	else:
		x=symbols(sym)

	f_func=input('Enter a f(x) function..:')
	a, b = input("Enter the value range..: ").split()
	ep=float(input("Enter the absolute relative error percentage..:"))
	epf=ep+1
	a=float(a)
	b=float(b)

	if a>b:
		a,b=b,a

	c,d=a,b

	f=sympify(f_func)
	f_diff=diff(f,x)

	if not (f.subs(x,a)*f.subs(x,b)<0):
		print("Sorry It is not possible to mention that the function has a root in the given range.")
	else: 
		x_prev=c
		i=0
		while ep<=epf :
			d1,d2=f.subs(x,x_prev),f_diff.subs(x,x_prev)
			x_next=x_prev-(d1/d2)
			epf=abs((x_next-x_prev)/x_next)*100
			x_prev=x_next
			i+=1

		print("Tolerance : {}% approximately one root of the equation : {}".format(epf,x_next))

except SympifyError:
	print("Please check for typos in the equation")
except ValueError:
	print("Value range cannot be entered empty, so an error occurred")
except Exception as e:
    print("Error!! type={} pls comment me this situtiaon :".format(type(e).__name__))