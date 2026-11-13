import numpy as np

def qr_decomposition(A: list[list[float]]) -> tuple[list[list[float]], list[list[float]]]:
    
    A = np.array(A, dtype=float)

    m, n = A.shape

    Q = np.zeros((m, n))
    R = np.zeros((n, n))

    for k in range(n):
        v = A[:, k].copy()


        for j in range(k):
            R[j, k] = np.dot(Q[:, j], A[:, k])
            v -= R[j, k] * Q[:, j]
        R[k, k] = np.linalg.norm(v)

        if np.isclose(R[k, k], 0):
            raise ValueError

        Q[:, k] = v / R[k, k]

    return Q, R
    pass