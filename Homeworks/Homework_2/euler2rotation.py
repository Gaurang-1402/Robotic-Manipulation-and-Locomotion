import numpy as np


#input the type of Euler angles
first_rotation = input('Define the typs of Euler angles: \n First rotation:')
second_rotation = input('Second rotation:')
third_rotation = input('Thrid rotation:')

#input the transformation:
theta1 = float(input("theta1:"))
theta2 = float(input("theta2:"))
theta3 = float(input("theta3:"))

#define the Euler angles and rotations
def rotation_matrix(input, theta):
    R = np.zeros([3,3])
    if input == 'Z':
        R = [[np.cos(theta),-np.sin(theta),0],[np.sin(theta),np.cos(theta),0],[0,0,1]]
    elif input == 'Y':
        R = [[np.cos(theta),0,np.sin(theta)],[0,1,0],[-np.sin(theta),0,np.cos(theta)]]
    elif input == 'X':
        R = [[1,0,0],[0,np.cos(theta),-np.sin(theta)],[0,np.sin(theta),np.cos(theta)]]
    return R

out = np.dot(rotation_matrix(first_rotation, theta1),rotation_matrix(second_rotation, theta2))
out = np.dot(out, rotation_matrix(third_rotation, theta3))
print(out)






