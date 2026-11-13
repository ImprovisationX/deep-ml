import numpy as np


def cholesky_decomposition(A):
    try:
        A = np.array(A, dtype=float)
        if A.ndim != 2:
            return -1

        m, n = A.shape

        if m != n or n == 0:
            return -1

        if not np.all(np.isfinite(A)):
            return -1

        if not np.allclose(A, A.T):
            return -1
        L = np.zeros((n, n))
        for i in range(n):
            for j in range(i + 1):

                s = A[i, j] - np.dot(L[i, :j], L[j, :j])

                if i == j:
                    if s <= 0:
                        return -1

                    L[i, j] = np.sqrt(s)

                else:
                    L[i, j] = s / L[j, j]

        return L.tolist()

    except (ValueError, TypeError, OverflowError):
        return -1
