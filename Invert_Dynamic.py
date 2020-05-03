
from scipy.optimize import fsolve
from math import cos,sin
import numpy as np
 
def f(theta):
    theta1 = float(theta[0])
    theta2 = float(theta[1])

    return [
        l1*cos(theta1)+l2*cos(theta1+theta2) - x1_,
        l1*sin(theta1)+l2*sin(theta1+theta2) - x2_,

    ]

l1 = 9
l2 = 9    
start = (2,6)
end = (12,3)
div = 10
x1 = np.arange(start[0],end[0],(end[0] - start[0])/div)
x2 = np.arange(start[1],end[1],(end[1] - start[1])/div)
for i in range(len(x1)):
	x1_,x2_= x1[i],x2[i]
	result = fsolve(f, [10, 10])
	print(result)