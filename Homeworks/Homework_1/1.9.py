import numpy as np
import matplotlib.pyplot as plt

from matrices_plotting import plot_two_axes, get_rotation_matrix_3d, plot_scatter_point, plot_vector

Aorigin = np.array([0, 0, 0])
X_A = np.array([1, 0, 0])
Y_A = np.array([0, 1, 0])
Z_A = np.array([0, 0, 1])

# ========================
# * offset of B origin from A origin (aka position vector, p)
p = p_idk = np.array([[-0.02783280], [-0.41963357], [0.23624219]])

# the code below is to flatten the list of lists for matplotlib plotting requirements 
Borigin_A = []
for sublist in p:
    Borigin_A.extend(sublist)

# theta = np.pi/3
R_x = R_idk = np.array([[-0.28005872, -0.50520401, -0.81629408], [-0.40937655, 0.83197963, -0.37446060], [0.86831904, 0.22930070, -0.43982182]])

point_1 = q1_in0 = np.array([[-0.32799012], [1.00892270], [0.22044525]])

point_2 = q1_in1 = np.array([[-0.15758880], [0.63601973], [0.02922015]])

point_3 = q2_in1 = np.array([[0.91762236], [-0.50850147], [0.40716952]])

possibilities = [(R_idk, p_idk), (R_idk.T, p_idk), (R_idk, -p_idk), (R_idk.T, -p_idk)]

for (R, p) in possibilities:
    zero_into_one = np.dot(R, point_1) + p.reshape(3, 1)
    
    if np.allclose(zero_into_one, point_2):
        print('found it')
        print(R)
        print(p)
        break
    
# Convert zero_into_one Rotation matrix and position vector to one_into_zero Rotation matrix and position vector

R_one_to_zero = R.T
p_one_to_zero = -np.dot(R.T, p)

q2_in0 = np.dot(R_one_to_zero, q2_in1) + p_one_to_zero.reshape(3, 1)
q2_in0

# q2_in1 = np.dot(R, q2_in1) + p.reshape(3, 1)
# q2_in1

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