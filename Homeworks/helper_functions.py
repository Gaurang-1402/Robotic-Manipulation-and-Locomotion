import numpy as np

get_skew = lambda a: np.array([[ 0, -a[2, 0], a[1, 0]], [a[2, 0], 0, -a[0, 0]], [-a[1, 0], a[0, 0], 0]])

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