#cowriter: Github Copilot
import numpy as np 
R01 = np.array([[-0.119365806805, -0.271075612465, -0.955128167574], [0.174448984216, -0.952766346110, 0.248603784415], [-0.977404397408, -0.136946347327, 0.161016588840]]) 
w0 = np.array([[0.420000000000], [-0.820000000000], [0.810000000000]]) 
t = 7.030000000000 
p1 = np.array([[1.060000000000], [2.330000000000], [-1.500000000000]])


#When asking for p1 and v1 in frame 1
#find w1 from w0
w1 = np.linalg.inv(R01) @ w0
#find skew symmetric matrix of w1
skew = np.array([[0,-w1[2,0],w1[1,0]],[w1[2,0],0,-w1[0,0]],[-w1[1,0],w1[0,0],0]])
#find the speed of p1 in frame 1
v1 = np.matmul(skew,p1)

#change v1 to be comma separated
v1 = np.array2string(v1, separator=',')
#change p1 to be comma separated
p1 = np.array2string(p1, separator=',')
print (v1)
print (p1)



#When asking for p0 and v0 in frame 0
w = w0*t
#find theta from w
theta = np.linalg.norm(w)
#find axis from w
axis = w/theta
#find skew symmetric matrix
skew = np.array([[0,-axis[2,0],axis[1,0]],[axis[2,0],0,-axis[0,0]],[-axis[1,0],axis[0,0],0]])
#find rotation matrix
R = np.eye(3) + np.sin(theta)*skew + (1-np.cos(theta))*np.dot(skew,skew)
#find position of p1 in frame 0 after rotation
p2 =   R @  R01 @ p1

#find skew symmetric matrix of w0
skew = np.array([[0,-w0[2,0],w0[1,0]],[w0[2,0],0,-w0[0,0]],[-w0[1,0],w0[0,0],0]])
#find the speed of p1 in frame 0
v0 = np.matmul(skew, p2)


#change v0 to be comma separated
v0 = np.array2string(v0, separator=',')
#change p2 to be comma separated
p2 = np.array2string(p2, separator=',')
print (v0)
print (p2)


