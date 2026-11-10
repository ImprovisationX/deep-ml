import numpy as np
def orthogonal_projection(v, L):
    v = np.array(v, dtype=float)
    L = np.array(L, dtype=float)

    alpha = np.dot(v, L)/np.dot(L, L)
    return alpha*L
    pass
