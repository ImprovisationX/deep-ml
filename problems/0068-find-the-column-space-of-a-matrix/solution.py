
import numpy as np

def matrix_image(A):
    pivot_cols = []
    for i in range(A.shape[1]):

        test_matrix = A[:, pivot_cols + [i]]
    
        if np.linalg.matrix_rank(test_matrix) > len(pivot_cols):
            pivot_cols.append(i)
            
    return A[:, pivot_cols].tolist()
