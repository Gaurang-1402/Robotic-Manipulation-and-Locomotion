import numpy as np

R_1in0 = np.array([[-0.785014617491, 0.586889316577, 0.198275012075], [-0.520247588576, -0.798342818557, 0.303300495614], [0.336295252578, 0.134943225643, 0.932038534046]])
sin_beta = R_1in0[2,0]
beta =  np.arcsin(-sin_beta)
alpha = -np.arccos(R_1in0[0,0]/np.cos(beta))
gamma = np.arcsin(R_1in0[2,1]/np.cos(beta))

print(alpha, beta, gamma)