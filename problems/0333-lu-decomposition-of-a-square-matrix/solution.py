import numpy as np

def lu_decomposition(A: list) -> tuple:
    A = np.array(A, dtype=float)

    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))

    for k in range(n):

        for j in range(k, n):
            U[k, j] = A[k, j] - np.dot(L[k, :k], U[:k, j])

        for i in range(k + 1, n):
            L[i, k] = (
                A[i, k] - np.dot(L[i, :k], U[:k, k])
            ) / U[k, k]

    return L, U   
    pass