import numpy as np

def cramers_rule(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)

    detA = np.linalg.det(A)
    if np.isclose(detA, 0):
        return -1
    rows, cols = A.shape
    x = np.zeros_like(b)

    for i in range(cols):
        A_tmp = A.copy()
        A_tmp[:, i] = b
        x[i] = np.linalg.det(A_tmp)/detA
    
    return x
    pass