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

def Rot(axis,theta):
	theta = trans2rad(theta)
	if axis == "z" or axis == "a":
		Rot_z= [ [np.cos(theta),-np.sin(theta),0,0],
					[np.sin(theta),np.cos(theta),0,0],
						[0,0,1,0],
							[0,0,0,1]
			]
		RotMat = Rot_z
	elif axis == "y" or axis == "o":
		Rot_y= [ [np.cos(theta),0,np.sin(theta),0],
					[0,1,0,0],
						[-np.sin(theta),0,np.cos(theta),0],
							[0,0,0,1]
				]
		RotMat = Rot_y
	elif axis =="x" or axis == "n":
		Rot_x= [ [1,0,0,0],
					[0,np.cos(theta),-np.sin(theta),0],
						[0,np.sin(theta),np.cos(theta),0],
							[0,0,0,1]
				]
		RotMat = Rot_x
	return RotMat

def Trans(x,y,z):
	TransMat= [ [1,0,0,x],
					[0,1,0,y],
						[0,0,1,z],
							[0,0,0,1]
			]	
	return TransMat

def matrix_inverse(T):
	return np.linalg.inv(T)

def multi_matrix_dot(mat1,mat2,mat3,mat4,mat_num):
	if mat_num == 4:
		mat_result = np.dot(np.dot(np.dot(mat1,mat2),mat3),mat4)
	elif mat_num == 3:
		mat_result = np.dot(np.dot(mat1,mat2),mat3)

	return mat_result

def defferitial_operator(T,dT):
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