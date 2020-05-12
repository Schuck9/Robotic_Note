import numpy as np

def mat_fourbyfour(mat1,mat2):
	transMat = np.matmul(mat1,mat2)
	# print(transMat)
	return transMat

def transition(T,transMat):
	return np.matmul(transMat,T) 

def trans2rad(degree):
	#np.cos/sin's input is rad/s
	return degree*np.pi/180

def normal_transition_mat():
	mat_z= [ [np.cos(0.15),-np.sin(0.15),0,0],
			[np.sin(0.15),np.cos(0.15),0,0],
				[0,0,1,0],
					[0,0,0,1]
			]
def matrix_inverse(T):
	return np.linalg.inv(T)


def defferitial_operator(T,dT)：
	#Δ = dT*T(^-1)
	return np.matmul(dT,np.linalg.inv(T))

def defferitial_operator_T(T,dT):
	#T^Δ = T(^-1)*dT
	return np.matmul(np.linalg.inv(T),dT)
	
if __name__ == '__main__':
	mat1 = [ [1,0,0,1],
				[0,1,0,2],
					[0,0,1,3],
						[0,0,0,1]
				]
	mat2= [ [1,0,0,1],
				[0,1,0,2],
					[0,0,1,3],
						[0,0,0,1]
				]
	T= [ [1,0,0,1],
				[0,1,0,2],
					[0,0,1,3],
						[0,0,0,1]
				]
	print("T after transiton:\n",transition(T,mat_fourbyfour(mat1,mat2)))