import sys
from sympy import *
try:
	sym=input('Your variable symbol:')
	if sym is None or sym=='':
		x=symbols('x')
	else:
		x=symbols(sym)

	func=input('Enter a function..:')
	a, b = input("Enter the value range..: ").split()
	ep=float(input("Enter the absolute relative error percentage..:"))
	epf=ep+1

	a=float(a)
	b=float(b)

	if a>b:
		a,b=b,a

	c,d=a,b

	f=sympify(func)

	if !(f.subs(x,a)*f.subs(x,b)<0):
		print("Sorry It is not possible to mention that the function has a root in the given range.")
	else: 
		while ep<=epf :
			d1,d2=f.subs(x,a),f.subs(x,b)
			x_r=b-((d2*a-d2*b)/(d1-d2))
			epf=((abs(x_r - a)/(x_r)) * 100)
			if f.subs(x,a)*f.subs(x,x_r)<0: 
				b=x_r
			elif f.subs(x,a)*f.subs(x,x_r)>0:
				a=x_r
			elif f.subs(x,a)*f.subs(x,x_r)==0:
				print("One root of the equation :{}".format(x_r))

		print("Tolerance : {}% approximately one root of the equation : {}".format(epf, x_r))

except SympifyError:
	print("Please check for typos in the equation")
except ValueError:
	print("Value range cannot be entered empty, so an error occurred")
except Exception as e:
    print("Error!! type={} pls comment me this situtiaon :".format(type(e).__name__))