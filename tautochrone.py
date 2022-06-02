# tautochrone-problem
import matplotlib.pyplot as plt 

from math import sqrt, cos , sin

import numpy as np 


def tautochrone(r): 
	x = [	] 
	y = [	] 
	for theta in np.linspace(0 , 1*np.pi,100):
		x.append(r*(theta - sin(theta))) 
		y.append(-r*(1 - cos(theta))) 
	plt.plot(x,y) 
	plt.show(	)
	
tautochrone(1) 
