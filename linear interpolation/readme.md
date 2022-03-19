
# Where is the Linear Interpolation Method Used? <br/>

The linear interpolation method is similar to the midpoint method.
not having an analytical solution with a nonlinear unknown
It is used to determine the roots of equations. <br/>

It is a closed interval method. The root of the range \[a,b\] is searched. <br/>

The purpose of this method is to distinguish the root thought to exist 
from the method of dividing into two. Faster approach. <br/>

Let y_0=f(a) and y_1=f(b) be x_0=a, x_1=b. (y_0,x_0) to (y_1,x_1) 
Equation of the line passing through its coordinates:  <br/>
It is found with the formula (y-y_0)/(x-x_0)=(y_1-y_0)/(x_1-x_0). 
If necessary adjustments are made as we get closer to y=0: <br/>

-y_0/(x-x_0)= (y_1-y_0)/(x_1-x_0) and <br/>
-y_0(x_1-x_0)/(y_1-y_0)=(x-x_0) so <br/>

It is seen that x=x_0-y_0(x_1-x_0)/(y_1-y_0). This value of x 
approaches the root of the equation.


[YouTube] ( https://www.youtube.com/watch?v=28F6NR0dX3A “YouTube”) <br/>
[Wikipedia] ( https://en.wikipedia.org/wiki/Linear_interpolation “WikiPedia”) <br/>
[Sympy] (https://docs.sympy.org/latest/index.html "Sympy Library Offical Documentation") <br/>

-[x] Check the bugs <br/>
-[x] Checking the continuity of the function <br/>