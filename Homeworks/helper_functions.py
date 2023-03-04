import numpy as np

get_skew = lambda a: np.array([[ 0, -a[2, 0], a[1, 0]], [a[2, 0], 0, -a[0, 0]], [-a[1, 0], a[0, 0], 0]])

def get_w_from_skew(skew):
    return np.array([[skew[2, 1]], [skew[0, 2]], [skew[1, 0]]])

get_linear_angular_velocity_from_twist = lambda twist: (twist[:3][:3], twist[3:][:3])

create_twist_from_linear_angular_velocity = lambda linear_velocity, angular_velocity: np.vstack((linear_velocity, angular_velocity))

def get_twist_skew(twist):
    w, v = get_linear_angular_velocity_from_twist(twist)
    w_skew = get_skew(w)
    twist_skew = np.zeros((4, 4))

    twist_skew[0:3, 0:3] = w_skew
    
    # ! twist_skew[:3, -1] returns a view of the last column of twist_skew but it is a row vector, v is a column vector
    # ! so we need to transpose v to make it a row vector and set it by reference
    twist_skew[:3, -1] = v.T

    return twist_skew

# Define the rotation matrices for each axis

def get_x_rotation_matrix(theta, is_hybrid = False):
    
    if is_hybrid:
        return np.array([
            [1, 0, 0, 0],
            [0, np.cos(theta), -np.sin(theta), 0],
            [0, np.sin(theta), np.cos(theta), 0],
            [0, 0, 0, 1]
        ])
    else:
        return np.array([[1, 0, 0],
                        [0, np.cos(theta), -np.sin(theta)],
                        [0, np.sin(theta), np.cos(theta)]])
    
def get_y_rotation_matrix(theta, is_hybrid = False):
    if is_hybrid:
        return np.array([
        [np.cos(theta), 0, np.sin(theta), 0],
        [0, 1, 0, 0],
        [-np.sin(theta), 0, np.cos(theta), 0],
        [0, 0, 0, 1]
    ])
    else:
        return np.array([[np.cos(theta), 0, np.sin(theta)],
               [0, 1, 0],
               [-np.sin(theta), 0, np.cos(theta)]])
    
def get_z_rotation_matrix(theta, is_hybrid = False):
    if is_hybrid:
        return np.array([
            [np.cos(theta), -np.sin(theta), 0, 0],
            [np.sin(theta), np.cos(theta), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])
    else:      
        return np.array([[np.cos(theta), -np.sin(theta), 0],
                [np.sin(theta), np.cos(theta), 0],
                [0, 0, 1]])