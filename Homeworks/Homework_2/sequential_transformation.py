import numpy as np

T_1in0 = np.array([[-0.38005242, -0.83109082, -0.40601504, 0.06597839], [0.46128050, -0.55076899, 0.69561039, 0.79693789], [-0.80173590, 0.07708159, 0.59268708, 0.28674595], [0.00000000, 0.00000000, 0.00000000, 1.00000000]])
T_3in0 = np.array([[0.37129013, -0.04616984, -0.92736831, -0.70701030], [0.67214077, 0.70243022, 0.23413367, 0.03934143], [0.64060162, -0.71025357, 0.29183804, -0.91083257], [0.00000000, 0.00000000, 0.00000000, 1.00000000]])

#Fine the inverse transformation of T_01
R_0in1 = np.transpose(T_1in0[:3,:3])
p_0in1 = -np.dot(R_0in1,T_1in0[:3,3].reshape(-1,1))
T_0in1 = np.concatenate((R_0in1, p_0in1),axis = 1)
T_0in1 = np.concatenate((T_0in1,[[0,0,0,1]]))

T_3in1 = np.dot(T_0in1 , T_3in0)
print(T_3in1)