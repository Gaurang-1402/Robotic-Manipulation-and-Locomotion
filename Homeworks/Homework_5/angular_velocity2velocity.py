#cowriter: Github Copilot
import numpy as np 
R01 = np.array([[-0.882524056769, 0.427920181548, 0.195027196689], [-0.101145567447, 0.232288125516, -0.967373661483], [-0.459261214789, -0.873456664620, -0.161717629285]])
w0 = np.array([[3.010000000000], [1.710000000000], [2.030000000000]]) 
t = 2.350000000000
p1 = np.array([[-2.930000000000], [-2.840000000000], [2.930000000000]])


lalaland = input("input v1 if you want v1p1, input v0 if you want v0p0:")

if lalaland == "v1":
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
    print ("v1", v1)
    print ("p1", p1)


if lalaland == "v0":
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
    print ("v0", v0)
    print ("p2", p2)


