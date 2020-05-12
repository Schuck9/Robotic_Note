import numpy as  numpy

def poly_3(t,Coef):

	return Coef[0] + Coef[1]*t + Coef[2]*(t**2) + Coef[3]*(t**3)

def poly_5(t,Coef):

	return Coef[0] + Coef[1]*t + Coef[2]*(t**2) + Coef[3]*(t**3) + Coef[4]*(t**4) + Coef[5]*(t**5)

if __name__ == '__main__':
	# C = [30,0,5.4,-0.72]
	C = [30,0,2.5,1.6,-0.58,0.0464]
	t_list = [1,2,3,4]
	for t in t_list:
		if len(C) == 4:
			print("t={},Ans={}".format(t,poly_3(t,C)))
		elif len(C) == 6:
			print("t={},Ans={}".format(t,poly_5(t,C)))