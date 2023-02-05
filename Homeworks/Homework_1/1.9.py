import numpy as np
import matplotlib.pyplot as plt

from matrices_plotting import plot_two_axes, rotation_matrix_3d, plot_scatter_point, plot_vector

Aorigin = np.array([0, 0, 0])
X_A = np.array([1, 0, 0])
Y_A = np.array([0, 1, 0])
Z_A = np.array([0, 0, 1])

# ========================

# * offset of B origin from A origin
Borigin_A = p_idk = np.array([-0.75658740, 0.18150963, 0.13073416])

# theta = np.pi/3
R_x = R_idk = np.array([[0.65762764, 0.75282666, 0.02789102], [-0.06765058, 0.02214137, 0.99746336], [0.75029946, -0.65784632, 0.06548994]])

point_1 = q1_in0 = np.array([[0.99596144], [0.53192520], [0.05159244]])

point_2 = q1_in1 = np.array([[-0.09889090], [0.90913361], [0.69246723]])

point_3 = q2_in1 = np.array([[-0.59616509], [0.77999788], [-0.85938971]])

[(R_idk, p_idk), (R_idk.T, p_idk), (R_idk, -p_idk), (R_idk, -p_idk)]


for (R, p) in [(R_idk, p_idk), (R_idk.T, p_idk), (R_idk, -p_idk), (R_idk, -p_idk)]:
    zero_into_one = np.dot(R, point_1) + p
    
    if np.allclose(zero_into_one, point_2):
        print('found it')
        print(R)
        print(p)
        break

# find out rotation matrix from 1 to 0
# use that to get the point q2_in0

# ========================

# find q_78
 
X_B, Y_B, Z_B = np.dot(R_x, [X_A, Y_A, Z_A])

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

plot_two_axes(ax, Aorigin, X_A, Y_A, Z_A, Borigin_A, X_B, Y_B, Z_B)
plot_scatter_point(ax, point_1, True, Aorigin, Borigin_A, 'g', marker_shape='o')
plot_scatter_point(ax, point_1, False, Aorigin, Borigin_A, 'pink', marker_shape='x')
# ".": point.
# "o": circle.
# "s": square.
# "^": triangle.
# "v": upside down triangle.
# "+": plus.
# "x": X.
# plot_scatter_point(ax, point_2, False, Aorigin, Borigin_A, 'c')
# plot_scatter_point(ax, point_3, False, Aorigin, Borigin_A, 'violet')





plt.show()